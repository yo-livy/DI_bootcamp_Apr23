// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);

//we will get an array of elements of all arrays. ['bread', 'carrot', 'potato', 'chicken', 'apple', 'orange']

// ------2------
const country = "USA";
console.log([...country]);

//we ll get an array of letters of strgin 'USA' --> ['U', 'S', 'A']

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);

//[undefined, undefdined], the spread syntax spreads the empty slots from the original array, resulting in undefined values in the new array.