import logo from './logo.svg';
import './App.css';
import BuggyCounter from './components/BuggyCounter';
import Color from './components/Color';
import ColorF from './components/ColorF';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <BuggyCounter /> */}
        {/* <Color /> */}
        <ColorF />
      </header>
    </div>
  );
};

export default App;
