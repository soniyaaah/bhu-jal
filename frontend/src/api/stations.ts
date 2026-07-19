import { useQuery } from '@tanstack/react-query';
import { apiClient } from './client';

export interface Station {
  id: string;
  name: string;
  latitude: number;
  longitude: number;
  district: string;
  created_at: string;
}

export interface GroundwaterReading {
  id: number;
  station_id: string;
  timestamp: string;
  water_level: number;
}

export const fetchStations = async (): Promise<Station[]> => {
  const { data } = await apiClient.get('/stations');
  return data;
};

export const fetchStationData = async (stationId: string): Promise<GroundwaterReading[]> => {
  const { data } = await apiClient.get(`/stations/${stationId}/data`);
  return data;
};

export const useStations = () => {
  return useQuery({
    queryKey: ['stations'],
    queryFn: fetchStations,
  });
};

export const useStationData = (stationId: string) => {
  return useQuery({
    queryKey: ['station-data', stationId],
    queryFn: () => fetchStationData(stationId),
    enabled: !!stationId,
  });
};
