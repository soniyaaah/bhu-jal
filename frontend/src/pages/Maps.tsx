import { useState, useMemo } from "react";
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useStations } from '../api/stations';
import { Link } from 'react-router-dom';
import L from 'leaflet';

import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
let DefaultIcon = L.icon({
    iconUrl: icon,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41]
});
L.Marker.prototype.options.icon = DefaultIcon;

export const Maps = () => {
  const { data: stations } = useStations();

  return (
    <div className="space-y-6 animate-in fade-in duration-500 h-[calc(100vh-80px)] flex flex-col">
      <div className="border-b border-gray-800 pb-5">
        <h1 className="text-3xl font-bold text-white tracking-tight">Geospatial Intelligence</h1>
        <p className="text-gray-400 mt-2">Interactive GIS mapping of all monitoring stations.</p>
      </div>

      <div className="flex-1 bg-[#1a1c23] border border-gray-800 rounded-xl overflow-hidden relative shadow-sm z-0">
        <MapContainer 
          center={[17.4065, 78.4772]} 
          zoom={11} 
          scrollWheelZoom={true} 
          style={{ height: '100%', width: '100%' }}
        >
          <TileLayer
            url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
          />
          
          {stations?.map((station) => (
            <Marker key={station.id} position={[station.latitude, station.longitude]}>
              <Popup>
                <div className="font-semibold text-gray-900">{station.name}</div>
                <div className="text-xs text-gray-500 mb-2">{station.district}</div>
                <Link to={`/stations/${station.id}`} className="text-cyan-600 text-xs font-medium hover:underline">
                  View Data &rarr;
                </Link>
              </Popup>
            </Marker>
          ))}
        </MapContainer>
      </div>
    </div>
  );
};
