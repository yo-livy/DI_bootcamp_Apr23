import bcrypt from 'bcrypt';
import { promises as fs } from 'fs'

const filePath = 'data.json'
let existingData = [{}];

export const _register = async (req, res) => {

    const first_name = req.body.first_name;
    const last_name = req.body.last_name;
    const username = req.body.username;
    const email = req.body.email.toLowerCase();
    const password = req.body.password + "";

    try {
        const data = {first_name, last_name, email, username, password};
        try {
            const dataFromFile = await fs.readFile(filePath, 'utf-8');
            existingData = JSON.parse(dataFromFile);
            console.log('existingData -> ', existingData);
        } catch (error) {
            console.log(error);
        }
        const dataExists = existingData.some(item => item.username === data.username);
        if (!dataExists) {
            existingData.push(data);
            console.log(existingData);
            await fs.writeFile(filePath, JSON.stringify(existingData, null, 2), 'utf-8');
            console.log('Data added to the file successfully.');
            return res.status(200).json('User added succesfully!');
        } else {
            console.log('User already exits');
            return res.status(400).json('User already exists');
        }
        
    } catch (error) {
        console.log(error);
        return res.status(404).json(error.message)
    }
}

export const _login = async (req, res) => {
    const username = req.body.username;
    const pass = req.body.password;

    try {
        const data = {username, pass}
        const dataFromFile = await fs.readFile(filePath, 'utf-8');
        existingData = JSON.parse(dataFromFile);
        const dataExists = existingData.some(item => item.username === data.username);
        if (dataExists) {
            return res.status(200).json('Login succesfully!');
        } else {
            return res.status(404).json('User not found');
        }      
          
    } catch (error) {
        console.log(error);
        return res.status(404).json(error);
    }
}