let text = document.getElementById("comments")
let result = document.getElementById("results")
const limit = 150
result.textContent = 0 + "/" + limit;

//COMMENT: function for enforced text limit
const textLimit = () =>{
    let textLength = text.value.length;
    result.textContent = textLength + "/" + limit;
    
    if(textLength >= limit){
        text.style.borderColor = 'red'
        result.style.color='red'
        result.textContent = `${textLength}/${limit} max character limit.`
    }
    else{
        text.style.borderColor = 'black'
        result.style.color='black'
    }
}


text.addEventListener("input", textLimit)