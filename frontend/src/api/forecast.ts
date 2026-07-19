import { useMutation } from '@tanstack/react-query';
import { apiClient } from './client';

export interface ForecastRequest {
  horizon_days: number;
  current_features: {
    water_level: number;
    temperature: number;
    precipitation: number;
  };
}

export interface ForecastResponse {
  station_id: string;
  forecast: Array<{
    target_date: string;
    predicted_water_level: number;
  }>;
}

export const generateForecast = async (stationId: string, req: ForecastRequest): Promise<ForecastResponse> => {
  const { data } = await apiClient.post(`/forecast/${stationId}`, req);
  return data;
};

export const useGenerateForecast = () => {
  return useMutation({
    mutationFn: ({ stationId, req }: { stationId: string; req: ForecastRequest }) => generateForecast(stationId, req),
  });
};
