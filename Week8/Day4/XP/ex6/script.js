console.log([2] === [2]) ; //false
console.log({} === {}); //false

// In JavaScript, when comparing objects or arrays using the strict equality operator (===), the comparison will return false if the operands are different objects or arrays, even if they have the same content.
// Each array and object is allocated a different memory reference, so they are not considered strictly equal.


const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number) // 4
console.log(object3.number) // 4
console.log(object4.number) // 5

class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mamal extends Animal {
    sound (animalSays) {
        return `${animalSays} I am the ${this.type}, named ${this.name} and I am ${this.color}`;
    }
}

const farmCow = new Mamal('moony', 'cow', 'black & white');
console.log(farmCow.sound('Moo'));