const isString = (str) => typeof str === 'string' ? true : false;

const a = isString('hello');
const b = isString(42);
const c = isString(['a', 'b', 'c']);

console.log(a);
console.log(b);
console.log(c);