const playTheGame = () => {
    const result = confirm('Would you like to play a game?');
    if (!result) {
        alert('No problem, goodbye!');
    } else {
        compareNumbers();
    }
}

const getUserNumber = () => {
    let userNumber = Number(prompt('Enter a number between 0 and 10'));
    while(true) {
        if (isNaN(userNumber) || userNumber == '') {
            alert('Sorry not a number, goodbye');
        } else if (userNumber > 10) {
            alert('Sorry it’s not a good number, goodbye');
        } else if (userNumber) {
            break;
        }
        userNumber = Number(prompt('Enter a number between 0 and 10'));
    }
    return userNumber;
}

const compareNumbers = () => {
    let i = 0;
    while (i < 3) {
        let computerNumber = Math.floor(Math.random() * 11);
        let userNumber = getUserNumber();
        if (!userNumber || userNumber > 10) {
            break;
        }
        alert(`Computer number ${computerNumber}`);
        if (userNumber === computerNumber) {
            alert('WINNER!');
            break;
        }
        if (userNumber > computerNumber) {
            if (i == 2) {
                alert('Out of chances');
                break;
            }
            alert('Your number is bigger then the computer’s, guess again');
        } else {
            if (i == 2) {
                alert('Out of chances');
                break;
            }
            alert('Your number is smaller then the computer’s, guess again');
            }
        i++;
}
}

