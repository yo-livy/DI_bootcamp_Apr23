import { useState } from 'react';
import './Todo.css';


const Todo = () => {
    const [inputValue, setInputValue] = useState('');
    const [todos, setTodos] = useState([]);

    const handleInputChange = (event) => {
        setInputValue(event.target.value)
    }

    const sendToTodo = (event) => {
        if(event.key === 'Enter'){
            setTodos([...todos, inputValue]);
            event.target.value = '';
        }
    }

    const delTodo = (index) => {
        const updatedTodos = [...todos];
        updatedTodos.splice(index, 1);
        setTodos(updatedTodos);
    }

    return (
        <div className='main'>
            <h1>Todo's</h1>
            {todos.map((item, index) => {
                return <div className='todo' key={index} onClick={() => delTodo(index)} >{item}</div>
            })}
            <div className='addContainer'>
                <p className='add'>Add new todo:</p>
                <input className='input' type="text" onChange={handleInputChange} onKeyDown={sendToTodo}/> 
            </div>
           
        </div>

    );
};

export default Todo;