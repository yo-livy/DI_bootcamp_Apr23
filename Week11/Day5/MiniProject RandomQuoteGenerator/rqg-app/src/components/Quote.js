import quotes from '../QuotesDatabase'
import { useState, useEffect } from 'react';
import './Quote.css'

const Quote = () => {
    const [randomQuotes, setRandomQuote] = useState({});
    const [prevQuoteIndex, setPrevQuoteIndex] = useState(null);
    const [color, setColor] = useState(null);
    const [key, setKey] = useState(0)

    const getRandomColor = () => {
        const red = Math.floor(Math.random() * 256);
        const blue = Math.floor(Math.random() * 256);
        const green = Math.floor(Math.random() * 256);

        const colorCode = `rgb(${red}, ${blue}, ${green})`;
        return colorCode;
    }

    const getRandomQuote = () => {
        let randIndx = Math.floor(Math.random() * quotes.length)

        while (randIndx === prevQuoteIndex) {
            randIndx = Math.floor(Math.random() * quotes.length);
        }

        setRandomQuote(quotes[randIndx]);
        setPrevQuoteIndex(randIndx);
        setColor(() => getRandomColor());
    }

    useEffect(() => {
        getRandomQuote();
    },[]);

    const handleButton = () => {
        getRandomQuote();
        setKey((prevState) => (prevState + 1))
    }


    return (
        <div className='main' style={{backgroundColor: color, transition: 'background-color 1.2s ease-in-out'}}>
            <div className="card-container">
                <div key={key} className='text-container'>
                    <h1 className="quote" style={{color:color}}>"{randomQuotes.quote}"</h1>
                    <h4 className="author" style={{color:color}}>-{randomQuotes.author}-</h4> 
                </div> 
                <div className="button-container">
                    <button className="new-quote-button" style={{ backgroundColor: color, transition : 'background-color 1.2s ease-in-out' }} onClick={handleButton}><b>New quote</b></button>
                </div>
            </div>
        </div>
  );
};

export default Quote;