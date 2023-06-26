function kilograms (num) {
    console.log(num * 1000);
};

kilograms(3);

const a = function (num) {
    console.log(num * 1000);
};

a(4);

const b = num => console.log(num*1000);

b(5);


//Function declaration: Function declarations are hoisted, meaning they can be invoked before they are declared in the code.

//Function expression: Function expressions are not hoisted and can only be invoked after they are defined in the code.


