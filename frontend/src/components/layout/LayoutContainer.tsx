import { useEffect } from "react";
import { Sidebar } from './Sidebar';
import { useWebSocket } from '../../hooks/useWebSocket';
import { useQueryClient } from '@tanstack/react-query';

export const LayoutContainer = ({ children }: { children: React.ReactNode }) => {
  const { lastMessage, isConnected } = useWebSocket('ws://localhost:8000/api/v1/ws');
  const queryClient = useQueryClient();

  useEffect(() => {
    if (lastMessage) {
      if (lastMessage.event === 'NEW_READING') {
        // Invalidate station data (history) and global stats
        queryClient.invalidateQueries({ queryKey: ['station-data'] });
        queryClient.invalidateQueries({ queryKey: ['stations'] });
      } else if (lastMessage.event === 'NEW_PREDICTION') {
        // Invalidate forecast data
        queryClient.invalidateQueries({ queryKey: ['forecast'] });
      }
    }
  }, [lastMessage, queryClient]);

  return (
    <div className="flex min-h-screen bg-[#111827]">
      <Sidebar />
      <main className="flex-1 ml-64 p-10 overflow-auto">
        <div className="flex justify-end mb-4">
          <div className={`px-3 py-1 rounded-full text-xs font-medium border flex items-center gap-2 ${isConnected ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' : 'bg-red-500/10 text-red-400 border-red-500/20'}`}>
             <div className={`w-2 h-2 rounded-full ${isConnected ? 'bg-emerald-400 animate-pulse' : 'bg-red-400'}`}></div>
             {isConnected ? 'Real-time Active' : 'Offline'}
          </div>
        </div>
        {children}
      </main>
    </div>
  );
};
