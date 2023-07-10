const http = require('http');


 const user = {
        firstname: 'John',
        lastname: 'Doe'
    }
const server = http.createServer((request, response) => {
   
    response.end(JSON.stringify(user));
});

server.listen(8080, () => {
    console.log('run on 8080');
});
