const newProm = new Promise((resolve) => {
    setTimeout(() => {
        resolve('success');
    }, 4000);
});

newProm.then((result) => {
    console.log(result);
})
