import { register, login, logUpdate } from "../models/usersModels.js";
import bcrypt from 'bcrypt';

export const _register = async (req, res) => {
    const first_name = req.body.first_name;
    const last_name = req.body.last_name;
    const username = req.body.username;
    const email = req.body.email.toLowerCase();
    const password = req.body.password + "";

    const salt = bcrypt.genSaltSync(10);
    const hash = bcrypt.hashSync(password, salt);

    try {
        const row = await register(first_name, last_name, email, username, hash);
        return res.status(200).json('User added succesfully!');
        
    } catch (error) {
        console.log(error);
        return res.status(404).json(error.message)
    }
}

export const _login = async (req, res) => {
    const username = req.body.username;
    const pass = req.body.password;

    try {
        const log = await login(username);
        
        if(log.length === 0){
            return res.status(404).json('User not found');
        }

        const match = await bcrypt.compare(pass + "", log[0].password);
            if (match) {
                await logUpdate(log[0].username);
                console.log('Last_login updated successfully!')
                return res.status(200).json('Login succesfully!');
            } else {
                return res.status(400).json("Password doesn't match. Try again");
            }

    } catch (error) {
        console.log(error);
        return res.status(404).json(error);
    }
}