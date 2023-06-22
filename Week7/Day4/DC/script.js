// const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'];
const planets = [
    {
        title: 'Mercury',
        moons: []
    },
    {
        title: 'Venus',
        moons: []
    },
    {
        title: 'Earth',
        moons: ['Moon']
    },
    {
        title: 'Mars',
        moons: ['Phobos', "Deimos"]
    },
    {
        title: 'Jupiter',
        moons: ['Io', 'Europe', 'Ganymed', 'Callisto']
    },
    {
        title: 'Saturn',
        moons: ['Titan', 'Enceladus', 'Mimas', 'Rhea']
    },
    {
        title: 'Uranus',
        moons: ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon']
    },
    {
        title: 'Neptune',
        moons: ['Triton', 'Proteus', 'Nereid']
    },
    {
        title: 'Pluto',
        moons: []
    },
]

for (let planet of planets) {
    const divPlanet = document.createElement('div');
    divPlanet.setAttribute('class', 'planet');
    const section = document.getElementsByClassName('listPlanets')
    section[0].appendChild(divPlanet);
    const getRandomRGB = () => {
        const r = Math.floor(Math.random() * 256); // Random value between 0 and 255
        const g = Math.floor(Math.random() * 256);
        const b = Math.floor(Math.random() * 256);
        const rgb = 'rgb(' + r + ', ' + g + ', ' + b + ')';
        return rgb;
      }
    divPlanet.style.backgroundColor = getRandomRGB();
    
    if (planet.moons.length !== 0) {
        let x = 150;
        for (let moon in planet.moons) {
            const divMoon = document.createElement('div');
            divMoon.setAttribute('class', 'moon');
            divPlanet.appendChild(divMoon);
            let leftX = String(x) + 'px';
            divMoon.style.left = leftX;
            x += 75;
            divMoon.style.top = '40px';
        }
    }
}