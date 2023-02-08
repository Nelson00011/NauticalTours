//profile

//REMOVE TRIP
function removeTrip(evt){
  evt.preventDefault();
const tripInput={
  trip_id: evt.target.value,
  intention: document.querySelector('#unselect').id,
}
console.log(tripInput)
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
console.log(evt.target.value)
document.querySelector(`#trip_id_${evt.target.value}`).remove();
});
}
//event listener remove trip
document.querySelector('#unselect').addEventListener('click', removeTrip) 
