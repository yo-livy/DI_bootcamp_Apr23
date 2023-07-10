const express = require('express');
const app = express();

app.listen(3001, () => {
    console.log(`server is listnening on port 3001`);
})
app.get('/', (req, res) => {
    res.send(`<h1>'This is a HTML tag'</h1>`);
})
