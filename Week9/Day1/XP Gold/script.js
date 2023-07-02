const sendData = (event) => {
    event.preventDefault();
    const nameValue = document.getElementById('name').value;
    const lastNameValue = document.getElementById('lastname').value;

    const newObj = {
        name : nameValue,
        lastname : lastNameValue
    }

    const jsonNewObj = JSON.stringify(newObj);

    const url = 'display.html?name=' + encodeURIComponent(nameValue) + '&lastname=' + encodeURIComponent(lastNameValue);

    window.location.href = url;


}