const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`


const toJs = () => {
    return new Promise ((resolve, reject) => {
        const objMorse = JSON.parse(morse); 
        if (Object.keys(objMorse).length === 0) {
            reject ('The json string is empty');
        } else {
            resolve(objMorse);
        }
    })
}

const toMorse = (objMorse) => {
    return new Promise ((resolve, reject) => {
        const askWord = prompt('Tell me the word');
        const askWordArr = askWord.toLowerCase().split('');
        const objMorseKeys = Object.keys(objMorse);
        const morseArr = [];
        
        askWordArr.forEach(element => {
            if (objMorseKeys.includes(element)) {
                morseArr.push(objMorse[element])
            } else {
            reject ('One of the character is not correct')
        }
        }); 
        resolve ([morseArr, askWord]);
    })
}

const joinWords = (morsetranslation, word) => {
    const wordNode = document.createElement('p');
    wordNode.textContent = `"${word}" gives you:`;
    document.body.appendChild(wordNode);
    morsetranslation.forEach((element) => {
        const pNode = document.createElement('p');
        pNode.textContent = element;
        document.body.appendChild(pNode);
    })
}

toJs()
.then(result => {
    return toMorse(result)
})
.then((array) => {
    return joinWords(array[0], array[1])
})
.catch((error) => {console.log(error)})
