const btn = document.getElementById('btn');
console.log(btn);

btn.addEventListener('click', changeColor);
function changeColor () {
    document.body.style.backgroundColor = 'lightgreen';
}

btn.addEventListener('mouseover', changeSize);
function changeSize () {
    btn.style.padding = '20px';
    btn.style.fontSize = '25px';
    btn.style.borderRadius = '1rem';
    btn.style.backgroundColor = 'yellow';
}

btn.addEventListener('mouseout', changePosition);
function changePosition () {
    btn.style.position = 'relative';
    btn.style.left = '100px';
    btn.style.top = '100px';
}

btn.addEventListener('dblclick', changeWeight);
function changeWeight () {
    btn.textContent = 'Bold';
    btn.style.fontWeight = 'bold';
}