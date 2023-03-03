//passcode requirements

var myInput = document.getElementById("psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {
    console.log("FIRSTCHILD TEST")
    console.log(letter.firstChild.classList)
    letter.firstChild.classList.remove("fa-remove")
    letter.firstChild.classList.add("fa-check")
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
    letter.firstChild.classList.add("fa-remove")
    letter.firstChild.classList.remove("fa-check")
}

  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {
    capital.firstChild.classList.remove("fa-remove")
    capital.firstChild.classList.add("fa-check")
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
    capital.firstChild.classList.add("fa-remove")
    capital.firstChild.classList.remove("fa-check")
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {
    number.firstChild.classList.remove("fa-remove")
    number.firstChild.classList.add("fa-check")
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
    number.firstChild.classList.add("fa-remove")
    number.firstChild.classList.remove("fa-check")
  }

  // Validate length
  if(myInput.value.length >= 8) {
    length.firstChild.classList.remove("fa-remove")
    length.firstChild.classList.add("fa-check")
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
    length.firstChild.classList.add("fa-remove")
    length.firstChild.classList.remove("fa-check")
  }
}