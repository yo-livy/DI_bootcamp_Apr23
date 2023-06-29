const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
];

const sectionNode = document.getElementById('section');

const viewRobots = (arr) => {
  arr.forEach((element) => {
    const divCard = document.createElement('div');
    sectionNode.appendChild(divCard);
    const divProfileContainer = document.createElement('div');
    divCard.appendChild(divProfileContainer);
          
    const imgProfile = document.createElement('img');
    divProfileContainer.appendChild(imgProfile);

    divCard.setAttribute('class', 'card')
    divProfileContainer.setAttribute('class', 'profile-container');
    imgProfile.setAttribute('class', 'image-profile');
    imgProfile.setAttribute('src', element['image']);
          
    const nameTextNode = document.createTextNode(element['name']);
    const nameNode = document.createElement('p');
    nameNode.appendChild(nameTextNode);
    divCard.appendChild(nameNode);
    nameNode.setAttribute('class', 'name');

    const mailTextNode = document.createTextNode(element['email']);
    const mailNode = document.createElement('p');
    mailNode.appendChild(mailTextNode);
    divCard.appendChild(mailNode);
    mailNode.setAttribute('class', 'mail');
  })
}

viewRobots(robots);

const input = document.getElementById('search');

input.addEventListener('input', () => {
  const inputValue = input.value.toLowerCase().trim();
  const filteredRobots = robots.filter((element) => element.name.toLowerCase().includes(inputValue));

  sectionNode.innerHTML = '';

  viewRobots(filteredRobots);
});