const express = require('express');
const app = express();

const user = {firstname: 'John',lastname: 'Doe'};

app.use('/', express.static(__dirname + '/public'));

app.listen(3000, () => {
    console.log(`server is listnening on port 3000`);
})

app.get('/users', (req, res) => {
    res.json(user);
})

app.get('/:id', (req, res) => {
    console.log(req.params);
    res.json(req.params);
});
