const makeAllCaps = (words) => {
    return new Promise ((resolve, reject) => {
        const newWords = words.map((word) => {
            if (typeof word === 'string') {
                return word.toUpperCase()
            } else {
                reject ('The string contain non-string element')
            }
        });
        resolve (newWords);
    })
}      

const sortWords = (words) => {
    return new Promise ((resolve, reject) => {
        if (words.length > 4) {
            resolve (words.sort());
        } else {
            reject ('The length is less than 4')
        }
    })
}


makeAllCaps([1, "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

makeAllCaps(["apple", "pear", "banana"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then((arr) => sortWords(arr))
    .then((result) => console.log(result))
    .catch(error => console.log(error))

