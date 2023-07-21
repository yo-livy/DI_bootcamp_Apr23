import db from '../config/db.js';

export const register = async (first_name, last_name, email, username, hash) => {
    const trx = await db.transaction();

    try {
        const answer = await trx('users').insert({first_name, last_name, email, username, last_login: new Date()}, ['user_id', 'first_name', 'last_name', 'email', 'username']);

        const login = await trx('login').insert({username, password: hash}, ['login_id', 'username', 'password']);

        await trx.commit();

        return answer;

    } catch (error) {
        console.log(error);
        await trx.rollback();
        throw error;
    }
}

export const login = async (username) => {
    try {
        const answer = await db('login').select('username', 'password').where({username});
        return answer;

    } catch (error) {
        console.log(error);
    }
}

export const logUpdate = async (username) => {
    try {
        const answer = db('users').update({last_login: new Date()}).where({username}).returning(['username', 'last_login']);
        return answer;
    } catch (error) {
        console.log(error);
    }
}