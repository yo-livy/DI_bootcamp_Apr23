// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// "inside the funcOne function 3". 'a' get a new value '3' in if-condition execution part, because the condition is true.

//--------------
// #1.1 - run in the console:

funcOne()

//return undefined and alert pop-up.

// #1.2 What will happen if the variable is declared 
// with const instead of let ?

//get an error since const 'a' cannot be assigned with another value.

//#2

let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

//the funcTwo will assign a new value to 'a'. It ll be 5. After it will be called.
//the funcThree will give a pop up message ' inside the funcThree function 5 '. Since it was reassigned in previous func. If it was called. Ifit wasn't the funcThree will pop up message with 0.

// #2.1 - run in the console:
funcThree()
funcTwo()
funcThree()
// #2.2 What will happen if the variable is declared 
// with const instead of let ?
// If we make const a = 0 - everytime we try to change its value we will get an error.

//#3
function funcFour() {
    window.a = "hello";
}
function funcFive() {
    alert(`inside the funcFive function ${a}`);
}
// as it assigned before as 5 we will get a = 5.

// #3.1 - run in the console:
funcFour()
funcFive()

//#4
const d = 1;
function funcSix() {
    let d = "test";
    alert(`inside the funcSix function ${d}`);
}

// we will get d = 'test' in alert pop up since the let variable is function scope.

// #4.1 - run in the console:
funcSix()
// #4.2 What will happen if the variable is declared 
// with const instead of let ?
//we will get the same result (d = 'test') since there are two different variables in two different scopes. 

//#5
const f = 2;
if (true) {
    const f = 5;
    alert(`in the if block ${f}`);
}
alert(`outside of the if block ${f}`);

// we will get two alerts: one of them with 5 and then with 2

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?
// nothing, the code will run the same result.

