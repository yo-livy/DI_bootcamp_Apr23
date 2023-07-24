import { useEffect, useState } from "react";
import ChildF from "./ChildF";


const ColorF = () => {
    const [favColor, setFavColor] = useState('red');
    const [show, setShow] = useState(true);

    useEffect (() => {
        setTimeout(() => {
            setFavColor('yellow')
        }, 3000);
        console.log('After update Color')
    }, [])

    const handleShow = () => {
        setShow(false);
    }

    return (
        <div>
            <h1>My favorite color is {favColor}</h1>
            {show && <ChildF />}
            <button onClick={handleShow}>Delete</button>
        </div>
    )
}

export default ColorF;