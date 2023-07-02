const anagram = (a, b) => {
    const aArr = a.toLowerCase().replace(/\s/g, '').split('');
    const bArr = b.toLowerCase().replace(/\s/g, '').split('');
    console.log(aArr);
    console.log(bArr);
    if(aArr.length === bArr.length && aArr.every((element) => bArr.includes(element))) {
        return true;
    } else {
        return false;
    }
}
console.log(anagram('he llo', 'ehllo'));