class Video {
    constructor (title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch () {
        console.log (`${this.uploader} watched all ${this.time} minutes of ${this.title} video!`);
    }

}

const videoOne = new Video('Wow', 'James', 25);
videoOne.watch();

const videoTwo = new Video('Fireworks', 'Scott', 12);
videoTwo.watch();

const fiveVideos = [
    ['First video', 'John', 11],
    ['Second video', 'Sam', 15],
    ['Third video', 'Jonny', 2],
    ['Fourth video', 'Monica', 3],
    ['Sixth video', 'Taylor', 2],
];

const newArr = [];

fiveVideos.forEach((element) => {
    newArr.push(new Video(...element));//If we are to pass the spread operator ...element as arguments to a class, it would treat each element of element array as separate arguments, not as an array.
})

console.log(newArr);
console.log(typeof newArr[0]);
