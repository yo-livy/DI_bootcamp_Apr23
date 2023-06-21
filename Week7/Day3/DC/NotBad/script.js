const sentence = 'The movie is not that bad, I like it';
console.log(sentence)
const wordNot = sentence.indexOf('not');
console.log(wordNot);
const wordBad = sentence.indexOf('bad');
console.log(wordBad);

if(wordBad > wordNot){
    let modifiedSentence = sentence.slice(0, wordNot) + 'good' + sentence.slice(wordBad + 3);
    console.log(modifiedSentence);
}else if(wordBad < wordNot && sentence.indexOf(wordBad) === -1 && sentence.indexOf(wordNot) === -1){
    console.log(modifiedSentence);
}
