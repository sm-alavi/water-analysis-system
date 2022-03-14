var wells = JSON.parse(document.getElementById('wells').textContent);
var map = L.map('map').setView([50, 50], 2);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFoZGlzbWEiLCJhIjoiY2wwOXp4c3BxMGlocDNrcXVldW9oNngzMSJ9.DWwhFVphtXti6OVuQUifFg', {
  //attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  //id:'mapbox.satellite-v9',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: 'pk.eyJ1IjoibWFoZGlzbWEiLCJhIjoiY2wwOXp4c3BxMGlocDNrcXVldW9oNngzMSJ9.DWwhFVphtXti6OVuQUifFg'
}).addTo(map);

wells.filter(function(well){return well.lat !== null }).map(function(well){
L.marker([well.lat, well.long])
.bindPopup(`
<div class="card m-n1 shadow-sm">
  <div class="card-header bg-dark text-white">
     ${well.name}
  </div>
  <div class="card-body">
    <table class="table table-striped m-n2">
      <tbody>
        <tr>
          <td>Field</td>
          <td>${well.field}</td>
        </tr>
        <tr>
          <td>Longitude</td>
          <td>${well.long}</td>
        </tr>
        <tr>
          <td>Latitude</td>
          <td>${well.lat}</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
`).bindTooltip(well.name, 
{
    permanent: true, 
    direction: 'right'
}).addTo(map);
})
