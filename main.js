const form = document.getElementById("earthquakeSearch");

form.addEventListener('submit', async function (event) {
    event.preventDefault();

    const startDate = document.getElementById("startDate").value;
    const endDate = document.getElementById("endDate").value;
    const minMag = document.getElementById("minMag").value;
    const maxMag = document.getElementById("maxMag").value;
    const naturalOnly = document.getElementById("natural").checked;

    const minTime = startDate ? new Date(`${startDate}T00:00:00.00Z`).getTime() : null;
    const maxTime = endDate ? new Date(`${endDate}T00:00:00.00Z`).getTime() : null;

    clearMarkers();

    const earthquakes = await window.getEarthquakes({
        minTime,
        maxTime,
        minMagnitude: minMag,
        maxMagnitude: maxMag,
        isEarthquake: naturalOnly ? true : undefined,
        limit: 70000,
    });


    console.log("eqs:", earthquakes);

    earthquakes.forEach((quake) => {
        addMarker(quake.y, quake.x, quake.mmi, quake.mag, quake.z);
    });
});





var map = L.map('map').setView([38.1187, -118.4751], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var markers = [];

function clearMarkers() {
    markers.forEach((marker) => {
        map.removeLayer(marker);
    });

    markers = [];
}
function addMarker(lat, long, mmi, mag, depth){
    if(mmi == null){
        estimatedMMI = 1.2 * mag - 1;
        if(estimatedMMI > 8){
            estimatedMMI = 8;
        }
        if(estimatedMMI < 2.5){
            estimatedMMI = 2.5;
        }
    }else{
        estimatedMMI = mmi
    }

    estimatedFeltRadius = (35*Math.E**(0.5*(mag-4)))*(estimatedMMI/4)**0.07+0.4*depth;
    
    console.log(estimatedFeltRadius)

    markers.push(L.circle([lat, long],{
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: estimatedFeltRadius*1000    
    }).addTo(map));
}

addMarker(35.2991666666667, -117.812333333333, 3.583, 3.55, 7.62);