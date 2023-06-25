const formNode = document.forms[0];
console.log(formNode);

const inputFName = document.forms[0].fname;
console.log(inputFName)
const inputLName = document.forms[0].lname;
console.log(inputLName)
const inputSubmit = document.forms[0].submit;
console.log(inputLName)

const inputFirstName = document.forms[0].firstname;
console.log(inputFName)
const inputLastName = document.forms[0].lastname;
console.log(inputLName)
const inputSubmittt = document.forms[0].submittt;
console.log(inputLName)

const myForm = document.forms[0];

myForm.addEventListener('submit', addLi);
function addLi (event) {
    event.preventDefault();
    const fName = this.firstname.value;
    const lName = this.lastname.value;

    const ulElement = document.querySelector('.usersAnswer');

    const liName = document.createElement('li');
    const liNameText = document.createTextNode(fName);
    liName.appendChild(liNameText);
    ulElement.appendChild(liName);

    const liLName = document.createElement('li');
    const liLNameText = document.createTextNode(lName);
    liLName.appendChild(liLNameText);
    ulElement.appendChild(liLName);
}