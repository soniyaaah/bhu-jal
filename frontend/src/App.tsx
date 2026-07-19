import { useState, useMemo } from "react";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { LayoutContainer } from './components/layout/LayoutContainer';
import { Dashboard } from './pages/Dashboard';
import { Stations } from './pages/Stations';
import { StationDetails } from './pages/StationDetails';
import { Forecast } from './pages/Forecast';
import { Maps } from './pages/Maps';
import { Analytics } from './pages/Analytics';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      staleTime: 5 * 60 * 1000,
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <LayoutContainer>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/stations" element={<Stations />} />
            <Route path="/stations/:id" element={<StationDetails />} />
            <Route path="/forecast" element={<Forecast />} />
            <Route path="/maps" element={<Maps />} />
            <Route path="/analytics" element={<Analytics />} />
          </Routes>
        </LayoutContainer>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App;
