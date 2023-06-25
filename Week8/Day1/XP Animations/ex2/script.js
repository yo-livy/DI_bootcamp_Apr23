const redSquare = document.getElementById('animate');
const yellowSquare = document.getElementById('container');
const redSquareWidth = parseInt(window.getComputedStyle(redSquare).width);
const yellowSquareWidth = parseInt(window.getComputedStyle(yellowSquare).width);
let intervalId;

function move() {
    currentLeft = parseInt(redSquare.style.left) || 0;
    
    if(currentLeft === (yellowSquareWidth - redSquareWidth)) {
        clearInterval(intervalId);
    } else {
        redSquare.style.left = (currentLeft + 10) + 'px';
    }
}
function myMove () {
    intervalId = setInterval(move, 100);
}


