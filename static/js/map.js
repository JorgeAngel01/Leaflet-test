
pk = "pk.eyJ1IjoiYW5nZWxzMDEwNyIsImEiOiJjbGJ2anRvdXAwdTMwM3ZxbzFkeWJndThqIn0.Ep3N8cDHH3Iwr9YLDgQn8g"

function initializeMap() {
  var initialCoordinates = [19.72293, -101.18551];
  var initialZoom = 18;

  var map = L.map("map").setView(initialCoordinates, initialZoom);

  // Add the base OpenStreetMap tile layer, can be changed to other tile layers
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
  }).addTo(map);

  return map;
}


function initializeRouteControl(map) {
  var control = L.Routing.control({
    waypoints: [],
    router: L.Routing.mapbox(
      pk,
      {
        profile: "mapbox/walking",
      }
    ),
    routeWhileDragging: true,
    show: false,
  }).addTo(map);

  return control;
}

function handleForm(map, control) {
  document.getElementById("route-form").addEventListener("submit", function (e) {
    e.preventDefault();

    var startSelect = document.getElementById("start");
    var endSelect = document.getElementById("end");

    var startValue = startSelect.value;
    var endValue = endSelect.value;

    if (startValue && endValue) {
      var startCoords = startValue.split(",");
      var endCoords = endValue.split(",");

      control.setWaypoints([
        L.latLng(parseFloat(startCoords[0]), parseFloat(startCoords[1])),
        L.latLng(parseFloat(endCoords[0]), parseFloat(endCoords[1])),
      ]);
    } else {
      alert("Selecciona un punto de inicio y uno de fin");
    }
  });
}

// Main function
function main() {
  var map = initializeMap();
  var control = initializeRouteControl(map);
  handleForm(map, control);
}

document.addEventListener("DOMContentLoaded", main);
