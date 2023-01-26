'use strict';

// We use a function declaration for initMap because we actually *do* need
// to rely on value-hoisting in this circumstance.

//fetch port variable

function initMap() {
  // coordinates to submit into the maps function

  const bayCoordinates = {
    lat: 37.601773,
    lng: -122.20287,
  };

  /*
  const coordinates = {
    bayCoordinates : {
        lat: 37.601773,
        lng: -122.20287,
      },
    hawaiiCoordinates: {
        lat: 0,
        lng: 0,
      },
    alaskaCoordinates: {
        lat: 0,
        lng: 0,
      },
    seattleCoordiantes: {
        lat: 0,
        lng: 0,
      }
  }
  */

// center and zoom required for maps line 13 to 16.
// initializing map itself Map(element, mapOption)
  const basicMap = new google.maps.Map(document.getElementById("map"), {
    center: bayCoordinates,
    zoom: 8,
  });

  //initializing marker option itself Marker(markerOptions)
  const sfMarker = new google.maps.Marker({
    position: bayCoordinates ,
    title: 'SF Bay',
    map: basicMap,
  });

  //add event listener when clicking on element
  sfMarker.addListener('click', () => {
    alert('Hi!');
  });

  //
  const sfInfo = new google.maps.InfoWindow({
    content: '<h1>San Francisco Bay!</h1>',
  });

  sfInfo.open(basicMap, sfMarker);

  const loco = [
    {
      name: 'Hackbright Academy',
      coords: {
        lat: 37.7887459,
        lng: -122.4115852,
      },
    },
    {
      name: 'Powell Street Station',
      coords: {
        lat: 37.7844605,
        lng: -122.4079702,
      },
    },
    {
      name: 'Montgomery Station',
      coords: {
        lat: 37.7894094,
        lng: -122.4013037,
      },
    },
  ];

  const markers = [];
  for (const location of loco) {
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

  for (const marker of markers) {
    const markerInfo = `
      <h1>${marker.title}</h1>
      <p>
        Located at: <code>${marker.position.lat()}</code>,
        <code>${marker.position.lng()}</code>
      </p>
    `;

    const infoWindow = new google.maps.InfoWindow({
      content: markerInfo,
      maxWidth: 200,
    });

    marker.addListener('click', () => {
      infoWindow.open(basicMap, marker);
    });
  }
}
