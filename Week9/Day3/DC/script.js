const search = async (event) => {
    console.log('start');
    event.preventDefault();
    const input = document.getElementById('category').value;
    console.log('Input', input);
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${input}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`);
        if (response.ok) {
            const data = await response.json();
            const divNode = document.createElement('div');
            document.body.appendChild(divNode);

            const container = document.createElement('div');
            divNode.appendChild(container);
            container.id = 'container';
            
            const imgNode = document.createElement('img');
            imgNode.src = data.data.images.original.url;
            container.appendChild(imgNode);

            const divBtn = document.createElement('div');
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.addEventListener('click', () => {
                container.remove();
              });
            divBtn.appendChild(deleteButton);
            container.appendChild(divBtn);
        }
    } catch (error) {
        console.log(error);
    }
}

const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', search);

const delAllBtn = document.getElementById('deleteAll');
delAllBtn.addEventListener('click', () => {
    const allContainers = document.querySelectorAll('#container');
    allContainers.forEach((element) => {
        element.remove();
    })
})
