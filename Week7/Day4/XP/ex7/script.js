const allBooks = [
    {
        title: 'Alice\'s Adventures in Wonderland',
        author: 'Lewis Carroll',
        image: 'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/fa761c72213835.5be04304160a1.png',
        alreadyRead: true
    },
    {
        title: 'The Lord of the Ring',
        author: 'J.R.R. Tolkien',
        image: 'https://cdn11.bigcommerce.com/s-gibnfyxosi/images/stencil/1920w/products/154740/156431/51eq24cRtRL__98083.1615576774.jpg?c=1',
        alreadyRead: false
    },
];

for (let book of allBooks) {
    const divNode = document.createElement('div');
    const img = document.createElement('img');
    const listBooks = document.getElementsByClassName('listBooks');
    listBooks[0].appendChild(divNode);
    listBooks[0].appendChild(img);
    const title = document.createTextNode(book['title']).textContent;
    const author = document.createTextNode(book['author']).textContent;
    const isRead = book['alreadyRead'];
    divNode.innerHTML = `${title} written by ${author}`;
    if (isRead) {
        divNode.style.backgroundColor = 'lightgreen'
    }
    img.setAttribute('src', book['image']),
    img.style.width = '100px'
}
