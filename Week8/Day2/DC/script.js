let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

const displayGroceries = () => {
    groceries['fruits'].forEach(element => {
        console.log(element);
    });
}
displayGroceries();

const cloneGroceries = () => {
    console.log(client);
    let user = client;
    client = 'Betty';
    console.log(user);
    console.log(client);
    console.log(user);
    let shopping = groceries;
    console.log(groceries);
    console.log(shopping);
    groceries['totalPrice'] = '35$';
    console.log(groceries);
    console.log(shopping); // it also changes because we copied the adress of the object, not the object itself.
    groceries['other']['payed'] = false;
    console.log(groceries);
    console.log(shopping);
}

cloneGroceries();

const newCloneOfGroceries = JSON.parse(JSON.stringify(groceries)); // method to clone the whole object, not the adress.

console.log(newCloneOfGroceries);
newCloneOfGroceries['totalPrice'] = '55$';

console.log(groceries);
console.log(newCloneOfGroceries);