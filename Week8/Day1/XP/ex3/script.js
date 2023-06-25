let allBoldItems;

function getAllBoldItems () {
    return document.querySelectorAll('b, strong');
}


function highlight () {
    allBoldItems = getAllBoldItems();
    for (const item of allBoldItems) {
        item.style.color = 'blue';
    }
}

function returnItemsToDefault () {
    allBoldItems = getAllBoldItems();
    for (const item of allBoldItems) {
        item.style.color = 'black';
    }
}

allBoldItems = getAllBoldItems();

for (const item of allBoldItems) {
    item.addEventListener('mouseover', highlight);
    item.addEventListener('mouseout', returnItemsToDefault);
}


