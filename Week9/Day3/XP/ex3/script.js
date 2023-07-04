// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));


const improve = async () => {
    try {
        const response = await fetch('https://www.swapi.tech/api/starships/9/');
        if (response.ok) {
            const objectStarWars = await response.json();
            console.log(objectStarWars.result);
          } else {
            throw new Error("issues with fetch");
          }
    } catch(error) {
        console.log(error)
    }
}

improve();