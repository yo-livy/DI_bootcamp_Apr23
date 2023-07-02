const urlParams = new URLSearchParams(window.location.search);

const name = urlParams.get('name');
const lastname = urlParams.get('lastname');

document.body.innerHTML = `Name: ${name}, Lastname: ${lastname}`