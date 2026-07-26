import api from "./api";
import type { PlaywrightScript } from "../types/Playwright";

export const generatePlaywright = async (
  projectId: number
): Promise<{ message: string }> => {
  const response = await api.post(`/playwright/${projectId}`);
  return response.data;
};

export const getPlaywrightScripts = async (
  projectId: number
): Promise<PlaywrightScript[]> => {
  const response = await api.get(`/playwright/${projectId}`);
  return response.data;
};