const myPromise = Promise.resolve(3);
const mySecondPromise = Promise.reject('boo!');

myPromise
.then((result) => {
    console.log(result);
})
.catch((error) => {
    console.log(error);
})

mySecondPromise
.then((result) => {
    console.log(result);
})
.catch((error) => {
    console.log(error);
})
