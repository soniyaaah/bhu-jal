import { useState, useMemo } from "react";
import { useStations } from '../api/stations';
import { Search, MapPin } from 'lucide-react';
import { Link } from 'react-router-dom';

export const Stations = () => {
  const { data: stations, isLoading } = useStations();
  const [searchTerm, setSearchTerm] = useState('');

  const filteredStations = stations?.filter(s => 
    s.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
    s.district.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-white tracking-tight">Station Management</h1>
          <p className="text-gray-400 mt-2">Monitor and configure physical sensor nodes.</p>
        </div>
        
        <div className="relative">
          <Search className="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-500" />
          <input 
            type="text" 
            placeholder="Search stations..." 
            className="w-full md:w-64 bg-[#1a1c23] border border-gray-700 text-white rounded-full py-2 pl-10 pr-4 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      <div className="bg-[#1a1c23] border border-gray-800 rounded-xl overflow-hidden shadow-sm">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-gray-800/50 border-b border-gray-800 text-xs uppercase tracking-wider text-gray-400 font-semibold">
              <th className="p-4">Station / Location</th>
              <th className="p-4">District</th>
              <th className="p-4">Coordinates</th>
              <th className="p-4 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {isLoading ? (
              <tr>
                <td colSpan={4} className="p-8 text-center text-gray-500">Loading stations...</td>
              </tr>
            ) : filteredStations?.length === 0 ? (
              <tr>
                <td colSpan={4} className="p-8 text-center text-gray-500">No stations found.</td>
              </tr>
            ) : (
              filteredStations?.map((station) => (
                <tr key={station.id} className="hover:bg-gray-800/30 transition-colors">
                  <td className="p-4">
                    <div className="flex items-center">
                      <div className="w-10 h-10 rounded-full bg-cyan-500/10 flex items-center justify-center mr-4 border border-cyan-500/20">
                        <MapPin className="w-5 h-5 text-cyan-400" />
                      </div>
                      <div>
                        <div className="font-medium text-white">{station.name}</div>
                        <div className="text-sm text-gray-500">ID: {station.id}</div>
                      </div>
                    </div>
                  </td>
                  <td className="p-4 text-gray-300">{station.district}</td>
                  <td className="p-4 text-gray-400 text-sm font-mono">
                    {station.latitude.toFixed(4)}, {station.longitude.toFixed(4)}
                  </td>
                  <td className="p-4 text-right">
                    <Link to={`/stations/${station.id}`} className="text-cyan-400 hover:text-cyan-300 text-sm font-medium">
                      View Details &rarr;
                    </Link>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};
