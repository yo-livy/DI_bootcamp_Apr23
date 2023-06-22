//Hi, Daniel! Here's week7 day 4 xp exercises (1 - 5 (5th without 'bonus' yet)). 
// The rest part of assignment (xp: 5th bonus, 6, 7 and Daily Challenge) I will upload a little bit later.


const divNode = document.getElementsByTagName('div')
console.log(divNode[0].innerHTML)

//--------

document.body.firstElementChild.nextElementSibling.children[1].innerHTML = 'Jason';

//--------

parentElement = document.body.children[2];
thirdChild = parentElement.children[2];
parentElement.removeChild(thirdChild);

//---------

const ulList = document.getElementsByClassName('list');
for (let i of ulList) {
    i.firstElementChild.innerHTML = 'Evgeny';
}

//---------

const ulElements = document.querySelectorAll('ul');
for (let i of ulElements) {
    i.classList.add('student_list')
}

//---------

const firstUl = document.body.children[1];
firstUl.classList.add('university', 'attendance');

//---------

const divNode1 = document.getElementById('container');
divNode1.style.backgroundColor = 'lightblue';
divNode1.style.padding = '10px';

//---------
const liElements = document.getElementsByTagName('li');
for (let i of liElements) {
    if (i.textContent === 'Dan') {
        i.style.display = 'none';
    }
}

//---------

for (let i of liElements) {
    if (i.textContent === 'Richard') {
        i.style.border = '1px solid green';
    }
}

//----------

document.body.style.fontSize = '50px';

//-----------

const firstName = document.getElementsByTagName('li')[0].textContent;
const secondName = document.getElementsByTagName('li')[1].textContent;
if (divNode1.style.backgroundColor === 'lightblue') {
    alert(`Hello ${firstName} and ${secondName}!`)
}
