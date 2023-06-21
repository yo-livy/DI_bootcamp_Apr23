for(let i = 1; i <+ 6; i++){
    console.log('* '.repeat(i));
}

let star = ''
for(let j = 0; j < 6; j++){
    for(let p = 0; p < j; p++){
        star += '* ';
    }
    star += '\n';
}
console.log(star);