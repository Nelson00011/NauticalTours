//profile

//REMOVE TRIP
function removeTrip(evt){
  evt.preventDefault();
const tripInput={
  trip_id: evt.target.value,
  intention: evt.target.classList[0],
}

fetch('/removeTrip', {
  method: 'POST',
  credentials: 'include',
  body: JSON.stringify(tripInput),
  headers: {
    'Content-Type': 'application/json',
  },
})
.then((res) => res.json())
.then((resJson) => {
alert(resJson.status);
//hide the removedTrips

document.querySelector(`#trip_id_${evt.target.value}`).remove();
//innerHtmlSetnew balance
document.querySelector("#balance").innerHTML=`Balance: $${resJson.balance}.00`
});
}
//event listener removeTrip
let unselected = document.querySelectorAll('.unselect')
unselected.forEach((button)=> button.addEventListener('click', removeTrip))
  
