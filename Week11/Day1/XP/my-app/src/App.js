import './App.css';
import UserFavouriteAnimals from './UserFavoriteAnimals.js';
import Exercise3 from './Exercise3.js';

const myelement = <h1>I Love JSX!</h1>;
const sum = 5 + 5;
const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Hello world!</p>
        {myelement}
        <p>React is {sum} times better with JSX</p>
        <h3>{user.firstName} {user.lastName}</h3>
        <UserFavouriteAnimals animals={user.favAnimals} />
        <Exercise3 />
      </header>
    </div>
  );
}

export default App;
