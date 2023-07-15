import express from "express";
import dotenv from "dotenv";
import path from 'path'
import router from "./routes/users.js";

const app = express();
dotenv.config();

app.use(express.urlencoded({extended:true}))
app.use(express.json())

const __dirname = path.resolve()
app.use('/', express.static(__dirname + '/public'));


app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`);
});

app.use(router);
