'use strict';
//COMMENT Insert filler into activities
const acts = {
    Honolulu: ["Paradise Cove Luau", "Pearl Harbor Museum", "Circle Island",  "Waikiki Buffet" , "Turtle Canyon Snorkeling", "Oahu Shark Dive", "Sunset Dinner Cruise", "Waikiki Atlantis", "Jurassic Adventure","Gem Waterfall"],
    Anchorage: ["Ice Cocktail Bar", "Wildlife Glacier Cafe", "Ice Moutain Biking",  "Scuba Dive" , "Mud Racing", "BlackBear Beer", "Salmon Fishing", "Wintervalley Fishing", "Scenic Bike Ride","Aurora Quest"],
    Seattle: ["Pike Place Market", "Space Needle Views", "Flight Museum",  "Great Wheel" , "Chihuly Gardens", "Post-Alley Gum Wall", "Fremont Toll", "Snoqualine Twin Falls", "Seattle Art Museum","Chocolate Tour"]
}

const allList=document.querySelectorAll(".featureInput")

for(let i=0;i<allList.length;i++){
    let element=document.getElementById(allList[i].id)
    let actList=[]
  
    const cacheList={}
    let currentList = acts[allList[i].id]
    
    while(8>actList.length){
        let index=Math.floor(Math.random()*currentList.length)
        let quote=currentList[index]

        if(!cacheList[quote]){
            actList.push(quote)
            cacheList[quote]=1
        }
    }
    actList = actList.map((c)=> `<li>${c}</li>`)
    element.innerHTML = actList.join("")
}

