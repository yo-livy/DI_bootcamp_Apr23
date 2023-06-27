const users = [
    { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
    { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
    { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
    { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
    { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
    { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
    { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}
];

console.log(users);

const welcomeStudents = users.map((element) => `Hello, ${element['firstName']}!`);
welcomeStudents.forEach((element) => console.log(element));

const onlyFSR = users.filter((element) => element['role'] === 'Full Stack Resident');
onlyFSR.forEach((element) => console.log(element));

const onlyFSRlastName = users.filter((element) => element['role'] === 'Full Stack Resident')
                             .map((element) => element['lastName']);
onlyFSRlastName.forEach((element) => console.log(element));