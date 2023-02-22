'use strict';
//COMMENT Insert random filler text into activities
const acts = {
    Honolulu: ["Local Submarine Trip", "Wildlife Cafe", "Home Brewed Beer",  "Scuba Dive" , "Dolphin Swim", "Canoe Trip with local Seals", "Ziplining From Vessel", "Barrel Boat Racing", "Hammock Swings from Lines","Darts on Deck"],
    Anchorage: ["Local Submarine Trip", "Wildlife Cafe", "Home Brewed Beer",  "Scuba Dive" , "Dolphin Swim", "Canoe Trip with local Seals", "Ziplining From Vessel", "Barrel Boat Racing", "Hammock Swings from Lines","Darts on Deck"],
    Seattle: ["Local Submarine Trip", "Visiting the Needle", "Home Brewed Beer",  "Scuba Dive" , "Dolphin Swim", "Canoe Trip with local Seals", "Ziplining From Vessel", "Barrel Boat Racing", "Hammock Swings from Lines","Darts on Deck"]
}

const allList=document.querySelectorAll(".featureInput")

for(let i=0;i<allList.length;i++){
    let element=document.getElementById(allList[i].id)
    let actList=[]
        
    const cacheList={}
    //COMMENT current list is the dictionary object
    //list of the current state
    let currentList = acts[allList[i].id]
    
    while(7>actList.length){
        let index=Math.floor(Math.random()*currentList.length)
        let quote=currentList[index]

        if(!cacheList[quote]){
            actList.push(quote)
            cacheList[quote]=1
        }
    }
    actList = actList.map((c)=> `<li>${c}</li>`)
    console.log(actList.join())
    element.innerHTML = actList.join("")
}

