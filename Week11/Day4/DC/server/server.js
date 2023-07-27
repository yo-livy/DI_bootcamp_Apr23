import express from 'express';
import cors from 'cors';

const app = express();
app.use(cors());

app.use(express.json()); // Parse JSON data
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded data


app.listen(3001, () => {
    console.log('run on port 3001');
});


app.get('/api/hello', (req, res) => {
    res.json('Hello From Express')
 });

app.post('/api/world', (req, res) => {
    console.log(req.body)
    res.json(`I received your POST request. This is what you sent me:${req.body.someName}`)
 });

