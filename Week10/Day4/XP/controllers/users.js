import { insertUser, loginUser } from "../models/users.js";

export const register = (req, res) => {
    insertUser(req.body)
      .then((user) => {
        res.json({ 
            message: 'Registration successful',
            id: user.user_id,
            first_name: user.first_name,
            last_name: user.last_name
        });
      })
      .catch((err) => {
        console.error(err);
        if (err.message === 'Email already exists' || err.message === 'Username already exists') {
          res.status(409).json({ message: err.message });
        } else {
          res.status(400).json({ message: 'Error occurred during user registration' });
        }
      });
  };
  
  export const login = (req, res) => {
    loginUser(req.body)
      .then((user) => {
        res.json({ message: 'Login successful', username: user.username });
      })
      .catch((err) => {
        console.error(err);
        res.status(400).json({ message: err.message });
      });
  };
