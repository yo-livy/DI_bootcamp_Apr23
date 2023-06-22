const change = [0.25, 0.1, 0.05, 0.01]

const changeEnough = (itemPrice, amountOfChange) => {
    let sum = 0;
    for (let i = 0; i < amountOfChange.length; i++) {
        const num = amountOfChange[i] * change[i];
        sum += num;
    }
    if (sum >= itemPrice) {
        return true;
    } else {
        return false;
    }
}

const price = 4.25;
const arr_change = [25, 20, 5, 0];
console.log(changeEnough(price, arr_change))



