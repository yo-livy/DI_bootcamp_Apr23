const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

const shoppingList = ['banana', 'orange', 'apple'];

const myBill = () => {
    let totalPrice = 0;
    for (let item of shoppingList) {
        for (let key in stock, prices) {
            if (item === key && stock[key] !== 0) {
                totalPrice += prices[key];
                stock[key]--;
            }
        }
    }
    console.log(totalPrice);
    console.log(stock)
}

myBill()