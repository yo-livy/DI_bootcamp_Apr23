import {useEffect, useState} from 'react';

const Color = () => {
    const [favColor, setFavColor] = useState('red');

    useEffect(() => {
        alert ('useEffect reached');
        // setFavColor('yellow')
    })

    const changeColor = () => {
        setFavColor('blue');
    }
    return (
        <div>
            <h1>My favorite color is {favColor}</h1>
            <button onClick={changeColor}>Change color</button>
        </div>
    )
}

export default Color;
