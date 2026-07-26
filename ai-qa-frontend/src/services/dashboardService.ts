import axios from "axios";
import type { DashboardSummary } from "../types/Dashboard";

const API_URL = "http://127.0.0.1:8000";

export const getDashboardSummary = async (): Promise<DashboardSummary> => {
  const token = localStorage.getItem("token");

  const response = await axios.get<DashboardSummary>(
    `${API_URL}/dashboard/summary`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return response.data;
};