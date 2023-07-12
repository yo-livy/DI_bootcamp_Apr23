const fs = require('fs')

fs.readFile('RightLeft.txt','utf-8', (err, data) => {
    if(err) return console.log(err);
    let position = 0;
    const arrRL = data.split('');
    console.log(arrRL);
    for(element of arrRL) {
        if(element === '>'){
            position++;
        } else if (element==='<') {
            position--;
        } else {
            continue;
        }
    }
    if (position > 0){
        console.log(`${position} steps to the right`)
    }else {
        (`${position} steps to the left`)
    }
});





fs.readFile('RightLeft.txt','utf-8', (err, data) => {
    if(err) return console.log(err);
    let position = 0;
    let totalSteps = 0
    const arrRL = data.split('');
    console.log(arrRL);
    for(let i = 0; i < data.length; i++){
        if(data[i] === '>'){
            position++;
        } else if(data[i] === '<') {
            position--;
        }
        totalSteps++;
        if(position === -1){
            break;
        }
    }
    console.log(totalSteps);
});

    