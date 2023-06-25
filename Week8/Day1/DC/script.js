const myForm = document.getElementById('libform');
const genStory = document.getElementById('story');

myForm.addEventListener('submit', getWords);

function getWords (event) {
    event.preventDefault();
    const noun = this.noun.value;
    const adjective = this.adjective.value;
    const person = this.person.value;
    const verb = this.verb.value;
    const place = this.place.value;
    if (!noun || !adjective || !person || !verb || !place) {
        alert('Please fill in all the inputs.');
        return;
    }
    const textNode = document.createTextNode(noun + adjective + person + verb + place);
    genStory.appendChild(textNode);
}





