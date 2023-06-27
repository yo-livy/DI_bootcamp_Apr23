const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

const colorChoices = colors.map((element, index) => {
    const ordinalIndex = (index + 1) > 3 ? 0 : index + 1;
    const choice = `${index + 1}${ordinal[ordinalIndex]} choice is ${element}`;
    return choice;
})

for(choice of colorChoices) {
    console.log(choice);
}
