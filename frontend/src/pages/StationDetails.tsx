import { useState, useMemo } from "react";
import { useParams, Link } from 'react-router-dom';
import { useStationData, useStations } from '../api/stations';
import { XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { ArrowLeft, Droplets, MapPin } from 'lucide-react';

export const StationDetails = () => {
  const { id } = useParams<{ id: string }>();
  const { data: stations } = useStations();
  const station = stations?.find(s => s.id === id);
  
  const { data: readings, isLoading } = useStationData(id || '');

  const stats = useMemo(() => {
    if (!readings || readings.length === 0) return null;
    let min = readings[0].water_level;
    let max = readings[0].water_level;
    let sum = 0;

    readings.forEach(r => {
      if (r.water_level < min) min = r.water_level;
      if (r.water_level > max) max = r.water_level;
      sum += r.water_level;
    });

    return {
      min: min.toFixed(2),
      max: max.toFixed(2),
      avg: (sum / readings.length).toFixed(2),
      latest: readings[readings.length - 1].water_level.toFixed(2),
      latestTime: new Date(readings[readings.length - 1].timestamp).toLocaleDateString()
    };
  }, [readings]);

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <Link to="/stations" className="text-cyan-400 hover:text-cyan-300 inline-flex items-center text-sm font-medium mb-4">
        <ArrowLeft className="w-4 h-4 mr-2" /> Back to Stations
      </Link>

      <div className="flex flex-col md:flex-row justify-between items-start md:items-end border-b border-gray-800 pb-5 gap-4">
        <div>
          <h1 className="text-3xl font-bold text-white tracking-tight">{station?.name || id}</h1>
          <div className="flex items-center text-gray-400 mt-2 space-x-4">
            <span className="flex items-center"><MapPin className="w-4 h-4 mr-1"/> {station?.district || 'Unknown District'}</span>
            <span className="flex items-center"><Droplets className="w-4 h-4 mr-1"/> Telemetry Active</span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-5 shadow-sm">
          <div className="text-sm font-medium text-gray-400 uppercase tracking-wider mb-1">Latest Reading</div>
          <div className="text-3xl font-light text-white">{stats?.latest || '--'} m</div>
          <div className="text-xs text-gray-500 mt-2">{stats?.latestTime || '--'}</div>
        </div>
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-5 shadow-sm">
          <div className="text-sm font-medium text-gray-400 uppercase tracking-wider mb-1">Historical Average</div>
          <div className="text-3xl font-light text-white">{stats?.avg || '--'} m</div>
        </div>
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-5 shadow-sm">
          <div className="text-sm font-medium text-gray-400 uppercase tracking-wider mb-1">Highest Level</div>
          <div className="text-3xl font-light text-white">{stats?.max || '--'} m</div>
        </div>
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-5 shadow-sm">
          <div className="text-sm font-medium text-gray-400 uppercase tracking-wider mb-1">Lowest Level</div>
          <div className="text-3xl font-light text-white">{stats?.min || '--'} m</div>
        </div>
      </div>

      <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
        <div className="mb-6">
          <h2 className="text-lg font-semibold text-white">Historical Telemetry</h2>
          <p className="text-sm text-gray-400">Complete time-series data for {station?.name}</p>
        </div>
        
        <div className="h-[500px] w-full">
          {isLoading ? (
            <div className="flex h-full items-center justify-center text-gray-500">Loading massive historical dataset...</div>
          ) : readings && readings.length > 0 ? (
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={readings}>
                <defs>
                  <linearGradient id="colorLevel" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#22d3ee" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#22d3ee" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" vertical={false} />
                <XAxis dataKey="timestamp" stroke="#9ca3af" tick={{fill: '#9ca3af', fontSize: 12}} tickFormatter={(t) => new Date(t).toLocaleDateString()} />
                <YAxis stroke="#9ca3af" tick={{fill: '#9ca3af', fontSize: 12}} domain={['dataMin', 'dataMax']} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1f2937', borderColor: '#374151', color: '#fff' }}
                  labelFormatter={(t) => new Date(t).toLocaleString()}
                />
                <Area type="monotone" dataKey="water_level" stroke="#22d3ee" strokeWidth={2} fillOpacity={1} fill="url(#colorLevel)" activeDot={{ r: 6 }} />
              </AreaChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex h-full items-center justify-center text-gray-500">No historical data available.</div>
          )}
        </div>
      </div>
    </div>
  );
};
