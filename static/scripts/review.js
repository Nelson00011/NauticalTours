
function colorChange(evt){
    //COMMENT: Changes Star Color Based on Position
    
    let num = evt.target.id
    num = num[4]*1
    for(let i=1; i<=5; i++){
      let star = document.getElementById(`star${i}`)
      star.style.color = i <= num ? 'gold':'black'  
   }
  }
  function mouseHover(evt){
    item_list=evt.target.style.cursor='pointer'
  }
  
  //COMMENT: star event listener
  let stars = document.querySelectorAll(".fa")
  stars.forEach((button) => button.addEventListener('click', colorChange))
  stars.forEach((button)=> button.addEventListener('mouseover', mouseHover))


  //COMMENT: submission form 
function submissionForm(evt){
let confirmation = document.querySelector('input[name="star"]:checked')
if(!confirmation){
  alert("Please Select Star Rating.")
}
}

  //COMMENT: event listener for each
  let btn = document.getElementById("submit")
  btn.addEventListener("click", submissionForm)