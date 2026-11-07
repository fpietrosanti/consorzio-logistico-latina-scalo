document.querySelectorAll('.leaflet-map[data-map]').forEach(function (el) {
  var d = JSON.parse(el.getAttribute('data-map'));
  var map = L.map(el, { scrollWheelZoom: false });
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map);
  L.circleMarker(d.hub, { radius: 9, color: '#d35400', fillColor: '#e67e22', fillOpacity: 1, weight: 2 })
    .addTo(map).bindTooltip(d.hubName);
  var bounds = [d.hub];
  d.points.forEach(function (p) {
    var m = L.circleMarker(p.c, { radius: 6, color: '#0f2b4a', fillColor: '#2670b0', fillOpacity: 0.9, weight: 1 }).addTo(map);
    m.bindTooltip(p.n);
    if (p.u) { m.on('click', function () { window.location.href = p.u; }); }
    bounds.push(p.c);
  });
  if (d.points.length === 1) {
    L.polyline([d.hub, d.points[0].c], { color: '#e67e22', weight: 2, dashArray: '6 6' }).addTo(map);
  }
  map.fitBounds(bounds, { padding: [30, 30], maxZoom: 12 });
});
