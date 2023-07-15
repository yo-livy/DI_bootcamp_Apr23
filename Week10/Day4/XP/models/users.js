import bcrypt from 'bcrypt';
import { db } from '../config/db.js';

export const insertUser = async ({ first_name, last_name, email, username, password }) => {
  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);

  // Check if email already exists
  const emailExists = await db('register').where({ email }).first();
  if (emailExists) {
    throw new Error('Email already exists');
  }

  // Check if username already exists
  const usernameExists = await db('register').where({ username }).first();
  if (usernameExists) {
    throw new Error('Username already exists');
  }

  const [result] = await db('register')
  .insert({
    first_name,
    last_name,
    email,
    username,
    password: hashedPassword,
    created_date: new Date(),
    last_login_date: new Date()
  })
  .returning('user_id');
  
  const { user_id } = result;

return {
  user_id,
  first_name,
  last_name,
}
};

export const loginUser = async ({ username, password }) => {
    // Check if user exists
    const user = await db('register').where({ username }).first();
    if (!user) {
      throw new Error('User does not exist');
    }
  
    // Check password
    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) {
      throw new Error('Invalid password');
    }
  
    // Update last login date
    await db('register')
      .where({ username })
      .update({ last_login_date: new Date() })
  
    // Add login details
    return db('login')
      .insert({
        username,
        password: user.password
      });
  };