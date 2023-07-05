class Quote {
    static idCounter = 0;
    static likeCounter = 0;
    constructor(author, quote) {
        this.id = Quote.idCounter++;
        this.author = author;
        this.quote = quote;
        this.like = Quote.likeCounter;
    }
}

const quotes = [
    new Quote('Mahatma Gandhi', 'Be the change that you wish to see in the world.', 0),
    new Quote('Mark Twain', 'Be the change that you wish to see in the world.', 0),
    new Quote('Leonardo da Vinci', 'Learning never exhausts the mind.', 0),
    new Quote('Mark Twain', 'I was educated once - it took me years to get over it.', 0),
    new Quote('Mark Twain', 'Give every day the chance to become the most beautiful day of your life.', 0)
]


const generateBtn = document.getElementById('generateBtn');
const sectionNode = document.getElementById('quoteSection');

let quoteTextNode = null;
let previousNumber = null;
let randomIndex = null;

generateBtn.addEventListener('click', (event) => {
    console.log('Hello');
    sectionNode.innerHTML = "";

    do {
        randomIndex = Math.floor(Math.random() * quotes.length);
    } while (randomIndex === previousNumber);
    console.log('Previous', previousNumber);
    previousNumber = randomIndex;
    console.log('Current', randomIndex);

    const randomQuote = quotes[randomIndex];
    const authorNode = document.createTextNode(randomQuote['author']);
    quoteTextNode = document.createTextNode(randomQuote['quote']);
    const p1Node = document.createElement('p');
    const p2Node = document.createElement('p');
    p2Node.style.fontSize = '32px';
    p1Node.appendChild(authorNode);
    p2Node.appendChild(quoteTextNode);
    sectionNode.appendChild(p1Node);
    sectionNode.appendChild(p2Node);
})

const addQuote = (event) => {
    event.preventDefault();
    const inputAuthor = document.getElementById('author').value;
    const inputQuote = document.getElementById('quote').value;
    const newQuote = new Quote(inputAuthor, inputQuote, 0);
    quotes.push(newQuote);
    console.log(quotes);
}


const countWithSpaces = () => {
    const text = quoteTextNode ? quoteTextNode.textContent : "";
    alert(`The number of chars inluding spaces is ${text.length}`);
}

const countWithoutSpaces = () => {
    const text = quoteTextNode ? quoteTextNode.textContent : "";
    alert(`The number of chars without spaces is ${
        text.replaceAll(' ', '').split('').length
    }`);
}

const wordsNumber = () => {
    const text = quoteTextNode ? quoteTextNode.textContent : '';
    if(text === ''){
        alert('No words');
    } else {
        alert(`The number of words is ${text.trim().split(' ').length}`);
    }
}

const likeQuote = () => {
    const text = quoteTextNode ? quoteTextNode.textContent : '';
    const index = quotes.findIndex(function(q) {
      return q.quote === text;
    });
    if (index !== -1) {
      quotes[index].like++;
      console.log("Liked the quote:", text);
      console.log("Total likes:", quotes[index].like);
    }
  }
  
  let filteredQuotes = [];
  let currentQuoteIndex = 0;
  
  const quoteForm = document.getElementById('quoteForm');
  const authorInput = document.getElementById('authorInput');
  const quoteText = document.getElementById('quoteText');
  const quoteAuthor = document.getElementById('quoteAuthor');
  const previousButton = document.getElementById('previousButton');
  const nextButton = document.getElementById('nextButton');
  
  quoteForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const inputValue = authorInput.value;
    filteredQuotes = quotes.filter((quote) => quote.author.toLowerCase() === inputValue.toLowerCase());
    currentQuoteIndex = 0;
    displayCurrentQuote();
  });
  
  previousButton.addEventListener('click', function () {
    if (currentQuoteIndex > 0) {
      currentQuoteIndex--;
      displayCurrentQuote();
    }
  });
  
  nextButton.addEventListener('click', function () {
    if (currentQuoteIndex < filteredQuotes.length - 1) {
      currentQuoteIndex++;
      displayCurrentQuote();
    }
  });
  
  function displayCurrentQuote() {
    const quote = filteredQuotes[currentQuoteIndex];
    quoteText.textContent = quote.quote;
    quoteAuthor.textContent = quote.author;
  }
  