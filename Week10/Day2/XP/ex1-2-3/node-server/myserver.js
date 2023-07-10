const http = require('http');

const server = http.createServer((request, response) => {
    response.end(`<div>
    <h1>This is my first response</h1>
    <h1>This is my second response</h1>
    <p>This is my third response</p>
    </div>`);
});

server.listen(3001, () => {
    console.log('run on 3001');
});
