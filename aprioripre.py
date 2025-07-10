import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("Amazon Sale Report.csv")
print(df.head(5))
# Order ID Qty Amount
segmentation_df=df[['Order ID','Qty','Amount']].dropna()
segmentation_df=segmentation_df.groupby('Order ID').agg({'Qty':'sum','Amount':'sum'}).reset_index()
scalar=StandardScaler()
scalar_data=scalar.fit_transform(segmentation_df[['Qty','Amount']])
pca=PCA()
pca_result=pca.fit_transform(scalar_data)
kmeans=KMeans(n_clusters=3,random_state=42)
clusters=kmeans.fit_predict(pca_result)
segmentation_df['cluster']=clusters
print(segmentation_df)


