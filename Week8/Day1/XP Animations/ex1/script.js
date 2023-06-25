function hello () {
    alert('Hello world!');
}

setTimeout(hello, 2000);

//--------------


function helloWorld () {
    const divNode = document.getElementById('container');
    const paragraphNode = document.createElement('p');
    const textNode = document.createTextNode('Hello world!');
    paragraphNode.appendChild(textNode);
    divNode.appendChild(paragraphNode);
}

setTimeout(helloWorld, 2000);


//---------------

let intervalId;
function startInterval () {
    intervalId = setInterval(helloWorld, 2000);
}
function stopInterval () {
    clearInterval(intervalId);
}
const stopBtn = document.getElementById('clear');
stopBtn.addEventListener('click', stopInterval);

startInterval();


