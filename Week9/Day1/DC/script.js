console.log('file');
const sendData = (event) => {
    event.preventDefault()
    console.log("test");
    const firstNameValue = document.getElementById('firstname').value;
    const lastNameValue = document.getElementById('lastname').value;

    const newObject = {
        name : firstNameValue,
        lastname : lastNameValue
    }

    console.log(newObject);

    const jsonNewObject = JSON.stringify(newObject);
    const textNode = document.createTextNode(jsonNewObject)
    const pNode = document.createElement('p');
    pNode.appendChild(textNode);
    document.body.appendChild(pNode);
}