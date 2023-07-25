import './App.css';
import EnteredInfo from './components/EnteredInfo';
import { useState } from 'react';

function App() {
  const [forminputs, setFormsinputs] = useState({});

  const handleChange = (e) => {
    const name = e.target.name;
    const value = e.target.type === "checkbox" ? e.target.checked : e.target.value;
    setFormsinputs({ ...forminputs, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const query = new URLSearchParams(formData).toString();
    console.log("query=>", `http://localhost:3000/?${query}`);
  }


  return (
    <div>
        <h1>Sample form</h1>
        <form onSubmit={(e) => handleSubmit(e)} >
          <input  name='fName' placeholder='First Name' onChange={handleChange} /><br/>
          <input name='lName' placeholder='Last Name' onChange={handleChange} /><br/>
          <input name='age' placeholder='Age' onChange={handleChange} /><br/>
          <br/>
          <input type="radio" name="gender" value="male" onChange={handleChange} /> Male<br/>
          <input type="radio" name="gender" value="female" onChange={handleChange} /> Female<br/>
          <h4>Select your destination:</h4>
          <select name='country' defaultValue="" onChange={handleChange}>
            <option value="">Please choose your destination</option>
            <option value="Japan">Japan</option>
            <option value="Thailand">Thailand</option>
            <option value="Brazil">Brazil</option>
          </select>
          <h4>Dietary restrictions</h4>
          <input type="checkbox" name="nutsFree" onChange={handleChange} /> Nuts Free<br/>
          <input type="checkbox" name="lactoseFree" onChange={handleChange} /> Lactose Free<br/>
          <input type="checkbox" name="vegan" onChange={handleChange} /> Vegan<br/><br/>

          <input type="submit" value="Submit" />

        </form>
        <EnteredInfo formData={forminputs}/>
    </div>
  );
}

export default App;
