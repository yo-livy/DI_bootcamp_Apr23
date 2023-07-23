import React, { useState } from 'react';
import Garage from './Garage';

const Cars = (props) => {
    const [color, setSolor] = useState('red');
  return (
    <div>
      <h1>This car is {color} {props.name}</h1>
      <Garage size='small'/>
    </div>
  )
}

export default Cars;
