const getGif = () => {
    fetch('https://api.giphy.com/v1/gifs/search?q=sun&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&limit=10&offset=2')
    .then(response => {
        if(response.ok) {
            return response.json()
        } else {
            throw new Error ("issues with fetch")
        }
    })
    .then(datagif => console.log(datagif))
    .catch(error => console.log(error))
}

console.log(getGif())