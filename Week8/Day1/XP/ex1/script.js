const h1Node = document.querySelector('h1');
console.log(h1Node.textContent);

const article = document.querySelector('article');
const paragraphs = article.getElementsByTagName('p');
const lastParagraph = paragraphs[paragraphs.length - 1];
lastParagraph.remove();

const h2Node = document.querySelector('h2');
h2Node.addEventListener('click', changeToGreen);

function changeToGreen() {
    h2Node.style.backgroundColor = 'red';
}

const h3Node = document.querySelector('h3');
h3Node.addEventListener('click', noDisplay);

function noDisplay() {
    h3Node.style.display = 'none';
}

const boldBtn = document.querySelector('#bold_btn');
boldBtn.addEventListener('click', turnBold);

function turnBold() {
    for (let i=0; i < paragraphs.length; i++) {
        paragraphs[i].style.fontWeight = 'bold';
    }
}

h1Node.addEventListener('mouseover', randomSize);
function randomSize() {
    const randomFontSize = Math.floor(Math.random()*101)
    this.style.fontSize = randomFontSize + 'px';
}

h1Node.addEventListener('mouseout', normalSize);
function normalSize() {
    this.style.fontSize = '2em';
}


paragraphs[1].addEventListener('mouseover', fadeIn);
function fadeIn() {
    this.style.transition = 'opacity 0.5s ease';
    this.style.opacity = 0;
  }

paragraphs[1].addEventListener('mouseout', fadeOut);
function fadeOut() {
    this.style.transition = 'opacity 0.5s ease';
    this.style.opacity = 1;
}