const displayNumbersDivisible = () => {
    let sum = 0;
    let output = '';
    for (let i = 0; i < 500; i++) {
        if (i % 23 === 0){
            output += (String(i) + ' '); 
            sum += i;
        }
    }
    console.log('Output: ', output);
    console.log('Sum: ', sum);
}
displayNumbersDivisible()


// -------------------------


