import { useState } from 'react';
import './App.css';


function App() {
  const [languages, setLanguages] = useState([{name: "Php", votes: 0}, {name: "Python", votes: 0}, {name: "JavaSript", votes: 0}, {name: "Java", votes: 0}]);

  const upVote = (index) => {
    setLanguages(languages.map((item, i) => {
      if (i === index) {
        return { ...item, votes: item.votes + 1 };
      }
      return item;
    }));
  };

      
  return (
    <div className="App">
      <header className="App-header">
        <h1>Vote your language!</h1>
        {
        languages.map((item, index) => {
          return (
          <div className='box'>
            <span>{item.votes}</span><span>{item.name}</span><button onClick={() => upVote(index)}>Click Here</button>
          </div>
          )
        })
      }
        
      </header>
    </div>
  );
}

export default App;
