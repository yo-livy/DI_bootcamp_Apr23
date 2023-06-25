const myForm = document.forms[0];
myForm.addEventListener('submit', getSolution);

function getSolution(event) {
    event.preventDefault();
    this.volume.value = ((4 / 3) * Math.PI * Math.pow(this.radius.value, 3)).toFixed(2);
}