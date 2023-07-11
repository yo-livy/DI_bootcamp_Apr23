const fs = require('fs');

fs.readFile('text.txt','utf-8', (err, data) => {
    if(err) return console.log(err);
    console.log(data);
})

fs.writeFile("data.txt", 'bla bla bla', "utf-8", (err) => {
    if (err) return console.log(err);
});

fs.appendFile("data.txt", ', \nmore bla bla bla', "utf-8", (err) => {
    if(err) return console.log(err);
});

fs.unlink("data.txt", (err) => {
    if (err) return console.log(err);
});