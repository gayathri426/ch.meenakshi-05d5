import{Routes,Route,Link,BrowserRouter as Router}
      from 'react-router-dom';
import './App.css';
import Home from './home';
import About from './about';
import Contact from './contact';

function App() {
  return (
    <Router>
      <Link to="/homepage" style={{margin:10}}>Home</Link>
      <Link to="/aboutpage"style={{margin:10}}>About us</Link>
      <Link to="/contactpage"style={{margin:10}}>Contact us</Link>
      <Routes>
        <Route path="/homepage" element={<Home/>}></Route>
        <Route path="/aboutpage" element={<About/>}></Route>
        <Route path="/contactpage" element={<Contact/>}></Route>
      </Routes>
    </Router>
  );
}

export default App;
