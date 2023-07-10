fetch('/users')
.then(res =>res.json())
.then(data => {
    console.log(data);
    document.getElementById('root').textContent = JSON.stringify(data);
})
.catch(e => {
    console.log(e);
});

const showAlert = () => {
    alert('Hello from JavaScript');
}

