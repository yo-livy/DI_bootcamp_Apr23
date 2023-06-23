const getNumber = () => {
    let number = Number(prompt('Enter the number'));
    if (isNaN(number) || number == '') {
        alert('Not a number');
    }
    return number;
}

let number = getNumber()
let i = 1;

const paragraphNode1 = document.createElement('p');
paragraphNode1.innerHTML = `We start the song at ${number} bottles<br>Take ${i} down, pass ${i > 1 ? 'them' : 'it'} around<br>We have now ${number -= i} ${number > 1 ? 'bottles' : 'bottle'}<br>`;
document.body.appendChild(paragraphNode1);
i++;

const paragraphNode2 = document.createElement('p');
paragraphNode2.innerHTML = `Take ${i} down, pass ${i > 1 ? 'them' : 'it'} around<br>We have now ${number -= i} ${number > 1 ? 'bottles' : 'bottle'}<br>`;
document.body.appendChild(paragraphNode2);
i++;

for (i; i < number; i++) {

    const paragraphNode = document.createElement('p');
    paragraphNode.innerHTML = `Then, take ${i} down, pass ${i > 1 ? 'them' : 'it'} around<br>We have now ${number -= i} ${number > 1 ? 'bottles' : 'bottle'}<br>`;
    document.body.appendChild(paragraphNode);
}
if (i > number) {
    const paragraphNode3 = document.createElement('p');
    paragraphNode3.innerHTML = `Then, take ${number} down, pass ${i > 1 ? 'them' : 'it'} around<br>We have now 0 bottle<br>`;
    document.body.appendChild(paragraphNode3);
}