import logo from './logo.svg';
import './App.css';
import ErrorBoundary from './components/ErrorBoundary';
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import HomeScreen from './components/HomeScreen';
import AboutScreen from './components/AboutScreen';
import ContactScreen from './components/ContactScreen';
import PostList from './components/PostList';
import Example1 from './components/Example1';
import Example2 from './components/Example2';
import Example3 from './components/Example3';
import FetchPost from './components/FetchPost';



function App() {
  return (
    <div style={{marginLeft:'50px'}}>
      <header>
        <ul className="nav nav-pills">
          <li className="nav-item">
            <NavLink className="nav-link" to="/">Home</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/about">About</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/contact">Contact</NavLink>
          </li>
        </ul>

      

       <Routes>
        <Route path='/' element={<ErrorBoundary><HomeScreen /></ErrorBoundary>} />
        <Route path='/about' element={<ErrorBoundary><AboutScreen /></ErrorBoundary>} />
        <Route path='/contact' element={<ErrorBoundary><ContactScreen /></ErrorBoundary>} /> 
       </Routes>

       <PostList />

       <Example1 />

       <Example2 />

       <Example3 />

      <FetchPost />
     
      </header>
    </div>
  );
};

export default App;
