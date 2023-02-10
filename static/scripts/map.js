'use strict';


//SAVE OR BOOK a trip AJAX
function generateTrip(evt){
  evt.preventDefault();
//grab information about tour, intention
  const formInputs = {
    tour_id: document.querySelector('p').id,
    intention: evt.target.value,
  };                   
console.log(formInputs)
//send to database to update
  fetch('/bookTrip', {
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify(formInputs),
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then((response) => response.json())
    .then((responseJson) => {
      alert(responseJson.status);
    });
};
//event listener for book_trip
document.querySelector('#booked').addEventListener('click', generateTrip) 
document.querySelector('#saved').addEventListener('click', generateTrip) 


//Google Maps API

//identify the class for map_port line 35
const map_port = document.querySelector('#map').classList[0]

// object of locations and 
const locations = {
  alaska: {
    port_id: "24",
    port_name: "Port of Anchorage",
    coordinates: {
      lat: 61.24114,
      lng: -149.88697
      
    },
    explore: [
      {
        name: 'Captain Cook Monument',
        coords: {
          lat: 61.2196327466289,
          lng:  -149.90393168657076,
        },
      },
      {
        name: '49th State Brewing',
        coords: {
          lat: 61.21999917650387, 
          lng: -149.89580257932107,
        },
      },
      {
        name: 'Anchorage Museum',
        coords: {
          lat: 61.21651599504423, 
          lng: -149.88562873269564,
        },
      },
      {
        name: 'Westchester Lagoon Nature Trail',
        coords: {
          lat: 61.205314923503266, 
          lng: -149.9038338693014,
        },
      },
      {
        name: 'Reindeer',
        coords: {
          lat: 61.21468272232086,  
          lng: -149.89983201341815
        },
      },
      {
        name: 'Planet Walk - Mars',
        coords: {
          lat: 61.218539089280085, 
          lng:-149.90655362762675
        },
      },
      {
        name: "Simon & Seafort's",
        coords: {
          lat: 61.218748715022606,
          lng:  -149.90468580898005,
        },
      },
    ]
  
  },
  // const hawaii =
  hawaii: {
    port_id: "39",
    port_name: "Port of Honolulu",
    coordinates: {
      lat: 21.3079761,
      lng: -157.866185
    },
    explore: [
      {
        name: 'Sand Island Beach',
        coords: {
          lat: 21.30044526763621,
          lng:  -157.8725776084272,
        },
      },
      {
        name: 'Foster Botanical Garden',
        coords: {
          lat: 21.320410785233012,
          lng: -157.85774231280183,
        },
      },
      {
        name: 'Aloha Tower',
        coords: {
          lat: 21.307904542660722, 
          lng: -157.8659632809965,
        },
      },
      {
        name: 'Iolani Palace',
        coords: {
          lat: 21.308038358462188, 
          lng:  -157.85868648134053,
        },
      },
      {
        name: 'Honolulu Museum of Art (HoMA)',
        coords: {
          lat: 21.304622117701328, 
          lng:  -157.84872575353768,
        },
      },
      {
        name: 'Café Julia Hawaii',
        coords: {
          lat: 21.30876664548009, 
          lng: -157.85976469653988,
        },
      },
      {
        name: "Nico's Pier 38",
        coords: {
          lat: 21.319271399471845,
          lng:  -157.87738680998638,
        },
      },
    ]
  },
  // const seattle =
  washington: {
    port_id: "30",
    port_name: "Port of Seattle",
    coordinates: {
      lat: 47.61707744883518, 
      lng: -122.36048698489884,
    },
    explore: [
      {
        name: 'Seattle Aquarium',
        coords: {
          lat: 47.60777477761617, 
          lng: -122.3431292447888,
        },
      },
      {
        name: 'The Seattle Great Wheel',
        coords: {
          lat: 47.606748964428306,
          lng: -122.34245843007986,
        },
      },
      {
        name: 'Space Needle',
        coords: {
          lat: 47.620647320082426,
          lng:  -122.34928275162737,
        },
      },
      {
        name: 'Umi Sake House',
        coords: {
          lat: 47.61391691779239, 
          lng: -122.34588361124976,
        },
      },
      {
        name: 'Seattle Art Museum',
        coords: {
          lat:47.60832042876705, 
          lng: -122.33789473851601 ,
        },
      },
      {
        name: 'Sound View Cafe',
        coords: {
          lat:47.61899851129625, 
          lng: -122.33934785381379, 
        },
      },
      {
        name: 'Black Bottle Gastrotavern',
        coords: {
          lat:47.61634922040611, 
          lng: -122.34969945397347,
        },
      },
    ]
  }
};


//identify the class for map_port line 35
const coordinate = locations[map_port]

//initiate google map function
function initMap() {
 
  const basicMap = new google.maps.Map(document.querySelector('#map'), {
    center: coordinate.coordinates,
    zoom: 13,
  });

  const portMarker = new google.maps.Marker({
    position: coordinate.coordinates,
    title: map_port,
    map: basicMap,
  });
//TODO:update intro
  const info = new google.maps.InfoWindow({
    content: `<h6>${coordinate.port_name}:</br></h6><p>Please Explore!</p>`,
  });

  info.open(basicMap, portMarker);

  //markers called
  const markers = [];
  for (const location of coordinate.explore) {
    markers.push(
      new google.maps.Marker({
        position: location.coords,
        title: location.name,
        map: basicMap,
        icon: {
          // custom icon
          url: '/static/img/marker.svg',
          scaledSize: {
            width: 30,
            height: 30,
          },
        },
      }),
    );
  }
//COMMENT event listener for markers
  for (const marker of markers) {
    const markerInfo = `<h6>${marker.title}</h6>`;
    const infoWindow = new google.maps.InfoWindow({
      content: markerInfo,
      maxWidth: 200,
    });

    marker.addListener('click', () => {
      infoWindow.open(basicMap, marker);
    });
  }

//COMMENT Google Places Library
//COMMENT query must be conditional based on buttons-

// put the code from "const request" to before the final bracket into a function that takes in SearchQuery
// call the function when one of the buttons is clicked, passing in the appropriate SearchQuery
// markers would need to be a global variable
// loop through markers and call marker.setMap(null) on each one
// create new markers
function buttonMap(evt=""){
  
  let target = evt.target.id
  let searchQuery = target[0].toUpperCase() + target.slice(1)

const request = {
  query: searchQuery,
  radius: '1500',
  location: coordinate.coordinates 
};

///COMMENT: gooogle services
var service = new google.maps.places.PlacesService(basicMap)

//COMMENT: generic infoWindow
const infoWindow = new google.maps.InfoWindow();

//COMMENT: list of markers here
const markerObj = {}


console.log(markerObj)
if(!markerObj[searchQuery]){
  markerObj[searchQuery] = []

service.textSearch(request, function(results, status) {
  if (status === google.maps.places.PlacesServiceStatus.OK) {
    for (let i = 0; i < results.length; i++) {
      //COMMENT: Create New Marker
      const markerMap = new google.maps.Marker({
        map: basicMap,
        title: results[i].name,
        position: results[i].geometry.location,
        icon: {
          url: results[i].icon,
          scaledSize: new google.maps.Size(25,25),
        },
      //COMMENT: specific colored icon to match button
      });
      
      markerObj[searchQuery] += markerMap
      console.log("DICITONARY/ OBJECT LINE 332")
      console.log(markerObj[searchQuery])
      //COMMENT: create contents
      const placeContent = `
      <div class="${searchQuery}" id='${results[i].place_id}'>
      <h5>${results[i].name}<h5>
      <p>${searchQuery} Rating: ${results[i].rating}</p>
      </div> 
      `
      //COMMENT: add eventlistener to every marker on map
      markerMap.addListener('click', () => {
        infoWindow.close();
        infoWindow.setContent(placeContent);
        infoWindow.open(basicMap, markerMap);
      });
    }
  }
});
//final bracket if statement

}
else{
// TODO: loop through map marks and make null
let markerList = markerObj[searchQuery]
console.log("MarkerLIST")
  console.log(markerList)
for(let i=0; i<markerList.length ;i++){
  let item = markerList[i]
  console.log("ITEMS LINE 356")
  console.log(item)
  item.setMap(null)
  markerObj[searchQuery]=[]
}
}
///buttonMap final bracket
}
///eventlisteners for each
document.querySelector('#museums').addEventListener('click', buttonMap) 
document.querySelector('#cafe').addEventListener('click', buttonMap) 
document.querySelector('#restaurants').addEventListener('click', buttonMap)


//final bracket
}








