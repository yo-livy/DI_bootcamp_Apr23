const inputUsername = document.getElementById('username');
const inputPassword = document.getElementById('password');

const submitButton = document.getElementById('loginButton');
const logMsg = document.getElementById('login-message');

const inputUsernameReg = document.getElementById('usernameReg');
const inputPasswordReg = document.getElementById('passwordReg');
const inputFName = document.getElementById('fName');
const inputLName = document.getElementById('lName');
const inputEmail = document.getElementById('email');

const submitButtonReg = document.getElementById('regButton');
const regMsg = document.getElementById('reg');

function checkLoginInput() {   
    if (inputUsername.value.trim() !== '' && inputPassword.value.trim() !== '') {
        submitButton.disabled = false;
        submitButton.style.backgroundColor = 'yellowgreen';
        submitButton.style.cursor = 'pointer';
    } else {
      submitButton.disabled = true;
      submitButton.style.backgroundColor = '';
      submitButton.style.cursor = '';
    }
}

function checkRegInput() {
  if (inputUsernameReg.value.trim() !== '' 
  && inputPasswordReg.value.trim() !== ''
  && inputFName.value.trim() !== ''
  && inputLName.value.trim() !== ''
  && inputEmail.value.trim() !== '') {
      submitButtonReg.disabled = false;
      submitButtonReg.style.backgroundColor = 'yellowgreen';
      submitButtonReg.style.cursor = 'pointer';
  } else {
    submitButtonReg.disabled = true;
    submitButtonReg.style.backgroundColor = '';
    submitButtonReg.style.cursor = '';
  }
}


const regUser = async () => {
  const data = { first_name: inputFName.value, last_name: inputLName.value, email: inputEmail.value, username: inputUsernameReg.value, password: inputPasswordReg.value }
  console.log(data);
  try {
    const response = await fetch('http://localhost:3000/register', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
      },
      body: JSON.stringify(data)
    });
    const parsedResponse = await response.json();
    if(response.status === 200){
      console.log(parsedResponse)
      regMsg.innerText = parsedResponse;
    } else {
      console.log(parsedResponse);
      regMsg.innerText = parsedResponse;
    }
  } catch (error) {
    console.log(error);
  }
}

submitButtonReg.addEventListener('click', regUser);



const logUser = async () => {
  const data = { username: inputUsername.value, password: inputPassword.value }
  console.log(data);
  try {
    const response = await fetch('http://localhost:3000/login', {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
      },
      body: JSON.stringify(data)
    });
    const parsedResponse = await response.json();
    logMsg.innerText = parsedResponse;
    // if(response.status === 200){
    //   console.log(parsedResponse)
    //   logMsg.innerText = parsedResponse;
    // } else {
    //   console.log(parsedResponse);
    //   logMsg.innerText = parsedResponse;
    // }
  } catch (error) {
    console.log(error);
  }
}

submitButton.addEventListener('click', logUser);