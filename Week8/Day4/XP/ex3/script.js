const users = { user1: 18273, user2: 92833, user3: 90315 };

const usersArray = Object.entries(users);

console.log(usersArray);
usersArray.forEach((element, index) => {
    usersArray[index][1] *= 2;
})
console.log(usersArray);


