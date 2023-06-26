((name) => {
    const divNode = document.createElement('div');
    const helloText = `Hello, ${name}!`;
    const textNode = document.createTextNode(helloText);
    
    divNode.appendChild(textNode);

    const img = document.createElement('img')
    img.setAttribute('src', 'https://bestprofilepictures.com/wp-content/uploads/2021/08/Amazing-Profile-Picture-for-Facebook.jpg');
    img.setAttribute('style', 'width: 100px; height: 100px');
    
    divNode.appendChild(img);

    const navbar = document.getElementById('navbar');
    navbar.appendChild(divNode);
})()