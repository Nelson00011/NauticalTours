//COMMENT: remove trip eventlistener
function removeTrip(evt){
  evt.preventDefault();
const tripInput={
  trip_id: evt.target.value,
  intention: evt.target.classList[0],
  action: evt.target.id
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
//COMMENT: hide the removedTrips

document.querySelector(`#trip_id_${evt.target.value}`).remove();
//COMMENT: innerHtmlSetnew balance
document.querySelector("#balance").innerHTML=`Balance: $${resJson.balance}.00`

}).catch((err)=>
console.log(err));
}
//COMMENT: event listener removeTrip
let unselected = document.querySelectorAll('.unselect')
unselected.forEach((button)=> button.addEventListener('click', removeTrip))
  
