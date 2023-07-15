function checkLoginInput() {
    const inputUsername = document.getElementById('username');
    const inputPassword = document.getElementById('password');
    const submitButton = document.getElementById('loginButton');
    
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
  const inputUsername = document.getElementById('usernameReg');
  const inputPassword = document.getElementById('passwordReg');
  const inputFName = document.getElementById('fName');
  const inputLName = document.getElementById('lName');
  const inputEmail = document.getElementById('email');

  const submitButton = document.getElementById('regButton');
  
  if (inputUsername.value.trim() !== '' 
  && inputPassword.value.trim() !== ''
  && inputFName.value.trim() !== ''
  && inputLName.value.trim() !== ''
  && inputEmail.value.trim() !== '') {
      submitButton.disabled = false;
      submitButton.style.backgroundColor = 'yellowgreen';
      submitButton.style.cursor = 'pointer';
  } else {
    submitButton.disabled = true;
    submitButton.style.backgroundColor = '';
    submitButton.style.cursor = '';
  }
}

const addUser = () => {
  
  let data = {
    first_name: document.getElementById('fName').value,
    last_name: document.getElementById('lName').value,
    email: document.getElementById('email').value,
    username: document.getElementById('usernameReg').value,
    password: document.getElementById('passwordReg').value
  }
  console.log(data);

  fetch('/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => {
      return response.json();
    })
    .then(data => {
      let message = data.message;
      if (data.id) {
        message = `OK! Hello ${data.first_name} ${data.last_name}. Your ID is ${data.id}`;
        document.getElementById('reg').innerText = message;
      } else {
        document.getElementById('reg').innerText = message;
      }
    })
    .catch((error) => {
      console.error('Error:', error);
      // Handle and display the registration error
      document.getElementById('reg').innerText = 'Registration error';
    });
  }  


const login = () => {
  let data = {
    username: document.getElementById('username').value,
    password: document.getElementById('password').value
  }

  fetch('/login', {
    method: 'POST', 
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
      let message = data.message;
      if (data.username) { // If username exists, login was successful
        message = `OK! Hello, your username is ${data.username}`;
      }
  
      document.getElementById('login-message').innerText = message;
  })
  .catch((error) => {
      console.error('Error:', error);
  });
}