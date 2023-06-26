const makeJuice = (size) => {
    const ingridients = [];
    const addIngridients = (a, b, c) => {
        // const text = `The client wants a ${size} juice, containing ${a}, ${b}, ${c}.`
        // const textNode = document.createTextNode(text);
        // const divNode = document.createElement('div');
        // divNode.appendChild(textNode);
        // document.body.appendChild(divNode);
        ingridients.push(a, b, c);
    }
    const displayJuice = () => {
        let text = `The client wants a ${size} juice, containing`;
        for (i of ingridients) {
            text += ` ${i} `;
        }
        const textNode = document.createTextNode(text);
        const divNode = document.createElement('div');
        divNode.appendChild(textNode);
        document.body.appendChild(divNode);
    }
    addIngridients('carrot', 'apple', 'orange');
    addIngridients('pineapple', 'pomegranade', 'strawberry');
    displayJuice();
}
makeJuice('medium');
