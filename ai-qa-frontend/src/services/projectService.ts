import api from "./api";
import type { Project } from "../types/Project";

export interface CreateProjectRequest {
  name: string;
  description: string;
  github_url: string;
}

export const getProjects = async (): Promise<Project[]> => {
  const response = await api.get("/projects/");
  return response.data;
};

export const createProject = async (
  project: CreateProjectRequest
): Promise<Project> => {
  const response = await api.post("/projects/", project);
  return response.data;
};

export const generateTests = async (
  projectId: number
): Promise<any> => {
  const response = await api.post(
    `/projects/${projectId}/generate-tests`
  );

  return response.data;
};