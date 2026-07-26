import api from "./api";

import type {
  ExecutionSummary,
  ExecutionHistory,
} from "../types/Execution";

/**
 * Execute Playwright tests
 */
export const executeProject = async (projectId: number) => {
  const response = await api.post(
    `/execute/${projectId}`
  );

  return response.data;
};

/**
 * Get execution summary
 */
export const getExecutionSummary = async (
  projectId: number
): Promise<ExecutionSummary> => {
  const response = await api.get(
    `/execute/${projectId}/summary`
  );

  return response.data;
};

/**
 * Get execution history
 */
export const getExecutionHistory = async (
  projectId: number
): Promise<ExecutionHistory[]> => {
  const response = await api.get(
    `/execute/${projectId}/history`
  );

  return response.data;
};