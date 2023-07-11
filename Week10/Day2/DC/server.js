const express = require('express');
const app = express();
app.use(express.json())

app.use(express.urlencoded({ extended: true }));

app.use('/', express.static(__dirname + '/public'))

app.listen(3001, () => {
    console.log(`server is listnening on port 3001`);
})


app.get('/aboutMe/:hobby', (req, res) => {
    const hobbyName = req.params.hobby
    if(isNaN(hobbyName)) {
        return res.status(200).json(req.params)
    } else {
        return res.status(404).json({msg: 'not found'});
    }
});

app.get('/pic', (req, res) => {
    res.send(`<div>
    <img src='https://images.unsplash.com/photo-1688976694262-89230d6133ba?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1287&q=80' alt='Some image'
    </div>`);
});

app.get('/form', (req, res) => {
    res.sendFile(__dirname + "/public/form.html");
});

app.post('/formData', (req, res) => {
    console.log(req.body);
    res.send(`Hello! My email is ${req.body.email} and my message is ${req.body.message}`)
});

