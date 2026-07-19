import { useState, useMemo } from "react";
import { useStations } from '../api/stations';
import { useGenerateForecast } from '../api/forecast';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { CloudRain, Thermometer, Activity } from 'lucide-react';

export const Forecast = () => {
  const { data: stations } = useStations();
  const [selectedStation, setSelectedStation] = useState('');
  const [horizon, setHorizon] = useState(30);
  
  const generateForecast = useGenerateForecast();
  
  const handlePredict = () => {
    if (!selectedStation) return;
    
    generateForecast.mutate({
      stationId: selectedStation,
      req: {
        horizon_days: horizon,
        current_features: {
          water_level: -5.0,
          temperature: 32.0,
          precipitation: 120.0
        }
      }
    });
  };

  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="border-b border-gray-800 pb-5">
        <h1 className="text-3xl font-bold text-white tracking-tight">Forecast Engine</h1>
        <p className="text-gray-400 mt-2">Predictive modeling for reservoir health & water availability.</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-1 space-y-6">
          <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
            <h3 className="text-lg font-semibold text-white mb-4">Configuration</h3>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-400 mb-1">Target Station</label>
                <select 
                  className="w-full bg-gray-800 border border-gray-700 text-white rounded-lg p-2.5 focus:border-cyan-500 focus:outline-none"
                  value={selectedStation}
                  onChange={(e) => setSelectedStation(e.target.value)}
                >
                  <option value="">Select a station...</option>
                  {stations?.map(s => (
                    <option key={s.id} value={s.id}>{s.name}</option>
                  ))}
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-400 mb-1">Horizon (Days): {horizon}</label>
                <input 
                  type="range" min="1" max="30" 
                  value={horizon} onChange={(e) => setHorizon(Number(e.target.value))}
                  className="w-full accent-cyan-500"
                />
              </div>

              <div className="pt-4 border-t border-gray-800">
                <button 
                  onClick={handlePredict}
                  disabled={!selectedStation || generateForecast.isPending}
                  className="w-full bg-cyan-600 hover:bg-cyan-500 text-white font-medium py-2.5 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex justify-center items-center"
                >
                  {generateForecast.isPending ? 'Generating...' : 'Run Prediction Model'}
                </button>
              </div>
            </div>
          </div>
          
          <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
            <h3 className="text-sm font-medium text-gray-400 mb-4 uppercase tracking-wide">Model Inputs (Static Demo)</h3>
            <div className="space-y-4">
              <div className="flex justify-between items-center">
                <div className="flex items-center text-gray-400"><CloudRain className="w-4 h-4 mr-2"/> Precipitation</div>
                <div className="text-white font-medium">120.0 mm</div>
              </div>
              <div className="flex justify-between items-center">
                <div className="flex items-center text-gray-400"><Thermometer className="w-4 h-4 mr-2"/> Avg Temp</div>
                <div className="text-white font-medium">32.0°C</div>
              </div>
            </div>
          </div>
        </div>

        <div className="lg:col-span-2">
          <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm h-[500px] flex flex-col">
            <h3 className="text-lg font-semibold text-white mb-6">Projection Results</h3>
            <div className="flex-1 w-full">
              {!generateForecast.data ? (
                <div className="flex h-full flex-col items-center justify-center text-gray-500">
                  <Activity className="w-12 h-12 mb-4 opacity-20" />
                  <p>Select a station and run the model to view forecast.</p>
                </div>
              ) : (
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={generateForecast.data.forecast}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" vertical={false} />
                    <XAxis dataKey="target_date" stroke="#9ca3af" tick={{fill: '#9ca3af', fontSize: 12}} tickFormatter={(t) => new Date(t).toLocaleDateString()} />
                    <YAxis stroke="#9ca3af" tick={{fill: '#9ca3af', fontSize: 12}} domain={['auto', 'auto']} />
                    <Tooltip 
                      contentStyle={{ backgroundColor: '#1f2937', borderColor: '#374151', color: '#fff' }}
                      labelFormatter={(t) => new Date(t).toLocaleDateString()}
                    />
                    <Line type="monotone" dataKey="predicted_water_level" stroke="#f59e0b" strokeWidth={3} strokeDasharray="5 5" activeDot={{ r: 6 }} />
                  </LineChart>
                </ResponsiveContainer>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
