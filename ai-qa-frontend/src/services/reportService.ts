import api from "./api";
import type { ReportSummary } from "../types/Report";

import type {
  PriorityDistribution,
  SeverityDistribution,
  TestTypeDistribution,
  ProjectDistribution,
} from "../types/Analytics";

export const getPriorityDistribution = async (): Promise<
  PriorityDistribution[]
> => {
  const response = await api.get("/reports/priority");
  return response.data;
};

export const getSeverityDistribution = async (): Promise<
  SeverityDistribution[]
> => {
  const response = await api.get("/reports/severity");
  return response.data;
};

export const getTestTypeDistribution = async (): Promise<
  TestTypeDistribution[]
> => {
  const response = await api.get("/reports/test-types");
  return response.data;
};

export const getProjectDistribution = async (): Promise<
  ProjectDistribution[]
> => {
  const response = await api.get("/reports/projects");
  return response.data;
};

export const getReportSummary = async (): Promise<ReportSummary> => {
  const response = await api.get("/reports/summary");
  return response.data;
};