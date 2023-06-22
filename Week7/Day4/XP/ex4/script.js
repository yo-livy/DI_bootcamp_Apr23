const hotelCost = () => {
    let totalPrice = 0;
    while (true) {
        const numNight = Number(prompt('How long would you like to stay: '));
        if (isNaN(numNight)) {
            continue;
        } else {
            totalPrice = numNight * 140;
            break;
        }
    } 
    return totalPrice;
}

const planeRideCost = () => {
    let price = 0;
    while (true) {
        const location = String(prompt('What is your destination: '));
        if (typeof location !== 'string') {
            continue;
        } else {
            if (location === 'London') {
                price = 183;
            } else if (location === 'Paris') {
                price = 220;
            } else {
                price = 300;
            }
            break;
        }
    } 
    return price;
}

const rentalCarCost = () => {
    let cost = 0;
    while (true) {
        const days = Number(prompt('For how many days you want to rent: '));
        if (isNaN(days)) {
            continue;
        } else {
            if (days <= 10) {
                cost = days * 40;
            } else {
                cost = days * 40 * 0,95;
            }
            break;
        }
    }
    return cost;
}

const totalVacationCost = () => {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();
  
    console.log('The hotel cost: $', hotel);
    console.log('The plane cost: $', plane);
    console.log('The car rent: $', car);
  
    const totalCost = hotel + plane + car;
    console.log('Total vacation cost: $', totalCost);
  };
  
  totalVacationCost();