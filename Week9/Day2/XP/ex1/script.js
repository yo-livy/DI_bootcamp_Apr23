const compareToTen = (num) => {
    const compareNum = new Promise ((resolve, reject) => {
        if (num <= 10) {
            resolve('Number is less or equal than 10')
        } else {
            reject('Number is more than 10')
        }
    })
    return compareNum
}
compareToTen(5)
.then ((result) => {
    console.log('Message', result);
})
.catch ((errror) => {
    console.log(error);
})

compareToTen(15)
.then ((result) => {
    console.log('Message', result);
})
.catch ((error) => {
    console.log(error);
})