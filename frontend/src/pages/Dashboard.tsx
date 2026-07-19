import { useState, useMemo } from "react";
import { useStations, useStationData } from '../api/stations';
import { Activity, Database, CheckCircle2, AlertCircle, BarChart2 } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export const Dashboard = () => {
  const { data: stations, isLoading: stationsLoading, isError: stationsError } = useStations();
  
  // Get data for the first station to show a sample chart and stats
  const sampleStation = stations?.[0];
  const { data: sampleData, isLoading: dataLoading } = useStationData(sampleStation?.id || '');

  const totalStations = stations?.length || 0;
  
  // Calculate average for the sample station
  const averageWaterLevel = useMemo(() => {
    if (!sampleData || sampleData.length === 0) return 0;
    const sum = sampleData.reduce((acc, curr) => acc + curr.water_level, 0);
    return (sum / sampleData.length).toFixed(2);
  }, [sampleData]);

  return (
    <div className="space-y-8 animate-in fade-in duration-500">
      <div className="border-b border-gray-800 pb-5">
        <h1 className="text-3xl font-bold text-white tracking-tight">Groundwater Intelligence Platform</h1>
        <p className="text-gray-400 mt-2">Hyderabad Monitoring System</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {/* Total Stations */}
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-medium text-gray-400 uppercase tracking-wider">Total Stations</h3>
            <Activity className="w-5 h-5 text-cyan-400" />
          </div>
          <div className="text-4xl font-light text-white">
            {stationsLoading ? '...' : totalStations}
          </div>
          <div className="mt-2 text-sm text-gray-500">Active monitoring nodes</div>
        </div>

        {/* Backend Status */}
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-medium text-gray-400 uppercase tracking-wider">Backend Status</h3>
            {stationsError ? (
               <AlertCircle className="w-5 h-5 text-red-400" />
            ) : (
               <CheckCircle2 className="w-5 h-5 text-green-400" />
            )}
          </div>
          <div className="text-3xl font-light text-white flex items-center">
             {stationsLoading ? '...' : (stationsError ? 'Offline' : 'Online')}
          </div>
          <div className="mt-2 text-sm text-gray-500">API Connection State</div>
        </div>

        {/* Avg Water Level (Sample) */}
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-medium text-gray-400 uppercase tracking-wider">Avg Water Level</h3>
            <BarChart2 className="w-5 h-5 text-cyan-400" />
          </div>
          <div className="text-4xl font-light text-white">
            {dataLoading ? '...' : (averageWaterLevel || '--')} <span className="text-lg text-gray-500">m</span>
          </div>
          <div className="mt-2 text-sm text-gray-500">Sampled from {sampleStation?.name || 'Network'}</div>
        </div>

        {/* Database Records (Sample) */}
        <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-medium text-gray-400 uppercase tracking-wider">Readings Synced</h3>
            <Database className="w-5 h-5 text-cyan-400" />
          </div>
          <div className="text-4xl font-light text-white">
            {dataLoading ? '...' : (sampleData?.length || 0)}
          </div>
          <div className="mt-2 text-sm text-gray-500">Records per standard station</div>
        </div>
      </div>

      {/* Main Chart Area */}
      <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-6 shadow-sm mt-8">
        <div className="mb-6">
          <h2 className="text-lg font-semibold text-white">Network Trend Sample</h2>
          <p className="text-sm text-gray-400">Recent telemetry data from active nodes</p>
        </div>
        
        <div className="h-[400px] w-full">
          {dataLoading ? (
            <div className="flex h-full items-center justify-center text-gray-500">Loading telemetry data...</div>
          ) : sampleData && sampleData.length > 0 ? (
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={sampleData.slice(-100)}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" vertical={false} />
                <XAxis dataKey="timestamp" stroke="#9ca3af" tick={{fill: '#9ca3af', fontSize: 12}} tickFormatter={(t) => new Date(t).toLocaleDateString()} />
                <YAxis stroke="#9ca3af" tick={{fill: '#9ca3af', fontSize: 12}} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1f2937', borderColor: '#374151', color: '#fff' }}
                  labelFormatter={(t) => new Date(t).toLocaleString()}
                />
                <Line type="monotone" dataKey="water_level" stroke="#22d3ee" strokeWidth={3} dot={false} activeDot={{ r: 6, fill: '#22d3ee' }} />
              </LineChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex h-full items-center justify-center text-gray-500">No data available to graph.</div>
          )}
        </div>
      </div>
    </div>
  );
};
