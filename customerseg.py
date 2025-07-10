import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data={
    'customerID':[1,2,3,4,5,6,7,8,9,10],
    'AnnualIncome':[15,16,17,60,20,90,45,78,32,56],
    'spendAmount':[55,88,44,77,66,22,33,45,78,96]
}
df=pd.DataFrame(data)
x=df[['AnnualIncome','spendAmount']]
kmeans=KMeans(n_clusters=3,random_state=42)
df['cluster']=kmeans.fit_predict(x)#fit will used for storing the data
print(df)
plt.figure(figsize=(8,6))
plt.scatter(df['AnnualIncome'],df['spendAmount'],c=df['cluster'],s=100)
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],c="red",s=200,marker="X")
plt.legend()
plt.grid(True)
plt.show()