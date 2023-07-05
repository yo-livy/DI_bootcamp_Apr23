const btn = document.getElementById('button');
const loading = document.getElementById('loading');
const output = document.getElementById('output');
const errorMsg = document.getElementById('error');


const fetchData = async () => {
    console.log('start')
    output.innerHTML = '';
    errorMsg.style.display = 'none';
    loading.style.display = 'block';
    const random = Math.floor(Math.random() * 83) + 1;
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${random}`);
        if(response.ok){
            const dataPerson = await response.json();
            console.log(dataPerson);
            const homeResponse = await fetch(dataPerson['result']['properties']['homeworld']);
            console.log(homeResponse);

            if(homeResponse.ok) {
                const homeData = await homeResponse.json()
                console.log(homeData);
                
                const textName = document.createTextNode(`Name: ${dataPerson['result']['properties']['name']}`);
                const textHeight = document.createTextNode(`Height: ${dataPerson['result']['properties']['height']}`);
                const textGender = document.createTextNode(`Gender: ${dataPerson['result']['properties']['gender']}`);
                const textBirth = document.createTextNode(`Birth Year: ${dataPerson['result']['properties']['birth_year']}`);
                const textHome = document.createTextNode(`Homeworld: ${homeData['result']['properties']['name']}`);
                    
                const pName = document.createElement('p');
                const pHeight = document.createElement('p');
                const pGender = document.createElement('p');
                const pBirth = document.createElement('p');
                const pHome = document.createElement('p');

                pName.appendChild(textName);
                pHeight.appendChild(textHeight);
                pGender.appendChild(textGender);
                pBirth.appendChild(textBirth);
                pHome.appendChild(textHome);

                output.appendChild(pName);
                output.appendChild(pHeight);
                output.appendChild(pGender);
                output.appendChild(pBirth);
                output.appendChild(pHome);
            } else {
                throw new Error('An error in 2nd fetch');
            }
        } else {
            throw new Error('An error in 1st fetch');
        }
    } catch (error) {
        errorMsg.style.display = 'block';
    } finally {
        loading.style.display = 'none';
    }
}
