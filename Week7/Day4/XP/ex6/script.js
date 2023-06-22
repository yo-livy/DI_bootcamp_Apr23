const divNode = document.getElementById('navBar');
divNode.setAttribute("id", "socialNetworkNavigation");

const liElement = document.createElement('li');
liElement.innerText = 'Logout';
const ulElement = document.getElementsByTagName('ul')[0];
ulElement.appendChild(liElement);

console.log(ulElement.firstElementChild.textContent);
console.log(ulElement.lastElementChild.textContent);