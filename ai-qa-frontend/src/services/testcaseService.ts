import api from "./api";
import type { TestCase } from "../types/TestCase";

export const getTestCases = async (
  projectId: number
): Promise<TestCase[]> => {
  const response = await api.get(`/testcases/${projectId}`);
  return response.data;
};