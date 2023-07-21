import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import router from './routes/router.js'

dotenv.config();

const app = express();
app.use(cors());
app.use(express.urlencoded({extended:true}));
app.use(express.json());
app.use(router);


app.listen(process.env.PORT, () => {
    console.log(`Listening on PORT ${process.env.PORT}`);
});