
function colorChange(evt){
    //to change the star color based on position
    //let color = evt.target.style.color
    let num = evt.target.id
    num = num[4]*1
    for(let i=1; i<=5; i++){
      let star = document.getElementById(`star${i}`)
      console.log(star)
      star.style.color = i <= num ? 'gold':'black'  
   }
  }
  
  function mouseHover(evt){
    item_list=evt.target.style.cursor='pointer'
  }
  
  
  //event listener
  let stars = document.querySelectorAll(".fa")
  stars.forEach((button) => button.addEventListener('click', colorChange))
  stars.forEach((button)=> button.addEventListener('mouseover', mouseHover))