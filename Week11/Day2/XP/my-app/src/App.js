import './App.css';
import Cars from './components/Cars';
import Color from './components/Color';
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
        <Color />
      </header>
    </div>
  );
}

export default App;
