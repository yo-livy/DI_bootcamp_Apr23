import { useState, useEffect } from 'react';
import heroes from '../superheroes.json';
import './Card.js'
import Card from './Card.js';
import './Superheroes.css';

const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

const Superheroes = () => {

    const [data, setData] = useState([]);
    const [points, setPoints] = useState(0);
    const [lastClickedId, setLastClickedId] = useState([]);
    const [topScore, setTopScore] = useState(0);

    useEffect(()=>{
        setData(shuffleArray(heroes.superheroes))
    })

    const handleScore = (id) => {
        if(!lastClickedId.includes(id)){
            setPoints(points + 1);
            setLastClickedId((prevState) => [...prevState, id]);
        }else{
            setTopScore((prevState) => (points > prevState ? points : prevState));
            setPoints(0);
            setLastClickedId([]);
        }
    }

    return (
        <div>
            <div className='title1'>
                <h1>Superheroes Memory Game</h1>
                <div className='scores'>
                    <span><b>Score:{points}</b></span> / <span><b>Top score:{topScore}</b></span>
                </div>
            </div>

            <div className='title2'>
                <h2>Get points by clicking on an image but don't click on any more than once!</h2>
            </div>

            <div className='main'>
                {data.map((item) => {
                return (
                    <div className='cardItem' key={item.id} onClick={() => handleScore(item.id)}><Card img={item.image} name={item.name} occupation={item.occupation}/></div>
                );
            })}
            </div>
       
        </div>
    );
};

export default Superheroes;