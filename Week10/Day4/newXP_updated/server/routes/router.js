import express from 'express';
import { _register, _login } from '../contorllers/usersControllers.js';

const router = express.Router();

router.post('/register', _register);
router.post('/login', _login);

export default router;