

function login(evt) {
    // TODO: Confirm User Login
    document.querySelector('#Account').innerHTML = "Congrats! You're Logged In.";
  };
  
document.querySelector('#login-button').addEventListener('click', login);
  


function register(evt) {
    // TODO: Confirm User Registration
    document.querySelector('#Account').innerHTML = "Congrats! You're Signed-Up and Logged In.";  
  };
  
document.querySelector('#sign-up').addEventListener('click', register);
  