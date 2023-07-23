import React, { useState } from 'react'

const Events = () => {
    const clickMe = () => {
        alert('I was clicked');
    }

    const handleKeyDown = (event) => {
        if(event.key === 'Enter'){
            const inputValue = event.target.value;
            alert(`You pressed Enter with input value ${inputValue}`);
        };
    };

    const [isToggleOn, setIsToggleOn] = useState(true);

    const toggle = () => {
        setIsToggleOn((prevState) => !prevState); //prevState is the current value of the isToggleOn. !prevState is the new one after executing the function.
    }

    return (
        <div>
            <button onClick={clickMe}>Click me!</button><br/>
            <input type="text" onKeyDown={handleKeyDown} /><br/>
            <button onClick={toggle}>{isToggleOn ? 'ON' : 'OFF'}</button>

        </div>
        )
};

export default Events
