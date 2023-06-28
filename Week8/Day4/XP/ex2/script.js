function displayStudentInfo(objUser){
    const {first, last} = objUser;
    const sentence = `Your full name is ${first} ${last}`;
    console.log(sentence);
}

displayStudentInfo({first: 'Elie', last:'Schoppik'});