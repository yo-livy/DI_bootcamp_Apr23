import './App.css';
import Cars from './components/Cars';
import Events from './components/Events';
import Phone from './components/Phone';

const carinfo = {name: "Ford", model: "Mustang"};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Cars name={carinfo.name} model={carinfo.model} />
        <Events />
        <Phone />
      </header>
    </div>
  );
}

export default App;
