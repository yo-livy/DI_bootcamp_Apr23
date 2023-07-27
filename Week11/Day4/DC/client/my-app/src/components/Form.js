import { useState } from "react";

const Form = () => {

    const [forminputs, setFormsinputs] = useState({});
    const [answer, setAnswer] = useState(null);

    const handleChange = (e) => {
      const name = e.target.name;
      const value = e.target.value;
      setFormsinputs({ ...forminputs, [name]: value });
      // console.log(forminputs);
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      const form = e.target;
      const formData = new FormData(form);
      const formDataObj = {};
      formData.forEach((value, key) => {
        formDataObj[key] = value;
      });
      try {
        const res = await fetch('http://localhost:3001/api/world',
        {
          method: 'POST',
          headers: {
            'content-type': 'application/json'
          }, 
          body: JSON.stringify(formDataObj)
        });
        const data = await res.json();
        setAnswer(data);
      } catch (error) {
        console.log(error)
      }
    }

    return (
      <div>
        <form onSubmit={handleSubmit}>
            <input name='someName' onChange={handleChange}/>
            <button type='submit'>Submit</button>
         </form>
         <p>{answer}</p>
      </div>
        
    )
}

export default Form;