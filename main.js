var map = L.map('map').setView([38.1187, -118.4751], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var markers = [];
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