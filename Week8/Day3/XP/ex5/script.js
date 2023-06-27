const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

const newString = epic.reduce((acc, currentValue) => acc + ' ' + currentValue, '');
console.log(newString);