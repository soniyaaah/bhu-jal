import { useState, useMemo } from "react";
import { BarChart3 } from 'lucide-react';

export const Analytics = () => {
  return (
    <div className="space-y-6 animate-in fade-in duration-500">
      <div className="border-b border-gray-800 pb-5">
        <h1 className="text-3xl font-bold text-white tracking-tight">Analytics Center</h1>
        <p className="text-gray-400 mt-2">Cross-station aggregations and long-term trend analysis.</p>
      </div>
      
      <div className="bg-[#1a1c23] border border-gray-800 rounded-xl p-12 text-center shadow-sm">
        <BarChart3 className="w-16 h-16 text-cyan-500/50 mx-auto mb-4" />
        <h3 className="text-xl font-medium text-white mb-2">Advanced Analytics in Development</h3>
        <p className="text-gray-400 max-w-md mx-auto">
          Complex multi-station aggregation, anomaly detection clustering, and reporting engines are scheduled for Phase 6. 
          Currently, please use the Dashboard and Station Details for analytics.
        </p>
      </div>
    </div>
  );
};
