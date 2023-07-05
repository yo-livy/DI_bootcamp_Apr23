const fCurrency = document.getElementById('fCurrency');
const sCurrency = document.getElementById('sCurrency');
const amount = document.getElementById('amount');
const output = document.getElementById('output');

let convert;
const getCurrency = async () => {
    const response = await fetch('https://v6.exchangerate-api.com/v6/1ef3bcf79e4cf51580d699fa/codes');
    if (response.ok) {
        const currencyData = await response.json();
        const supportedCurrency = currencyData.supported_codes;
        const selectCurrency = supportedCurrency.map((element) => element[0]);
        selectCurrency.forEach(element => {
            const option = document.createElement('option');
            option.textContent = element;
            fCurrency.appendChild(option);
            sCurrency.appendChild(option.cloneNode(true));
       
        }); 
        convert = async (event) => {
            event.preventDefault();
            const response = await fetch(`https://v6.exchangerate-api.com/v6/1ef3bcf79e4cf51580d699fa/pair/${fCurrency.value}/${sCurrency.value}/${amount.value}`);
            if (response.ok) {
                const resultData = await response.json();
                const result = resultData.conversion_result;
                const pNode = document.createElement('p');
                pNode.textContent = result;
                output.appendChild(pNode);
    }
    }
}
}

getCurrency();







