import logo from './logo.svg';
import './App.css';
import BuggyCounter from './components/BuggyCounter';
import Color from './components/Color';
import ColorF from './components/ColorF';
import ErrorBoundary from './components/ErrorBoundary';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ErrorBoundary>
          <BuggyCounter />
          <BuggyCounter />
        </ErrorBoundary>
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>
        <BuggyCounter />
        
        
        {/* <Color /> */}
        {/* <ColorF /> */}
      </header>
    </div>
  );
};

export default App;
