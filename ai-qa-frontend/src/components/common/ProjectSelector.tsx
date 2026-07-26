import { useEffect } from "react";
import {
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  CircularProgress,
} from "@mui/material";

import { useProject } from "../../context/ProjectContext";
import { getProjects } from "../../services/projectService";

export default function ProjectSelector() {
  const {
    projects,
    setProjects,
    selectedProject,
    setSelectedProject,
  } = useProject();

  useEffect(() => {
    const loadProjects = async () => {
      try {
        const data = await getProjects();

        setProjects(data);

        if (!selectedProject && data.length > 0) {
          setSelectedProject(data[0]);
        }
      } catch (error) {
        console.error("Failed to load projects:", error);
      }
    };

    loadProjects();
  }, []);

  if (projects.length === 0) {
    return <CircularProgress size={24} />;
  }

  return (
    <FormControl size="small" sx={{ minWidth: 260 }}>
      <InputLabel>Current Project</InputLabel>

      <Select
        value={selectedProject?.id ?? ""}
        label="Current Project"
        onChange={(e) => {
          const project = projects.find(
            (p) => p.id === Number(e.target.value)
          );

          if (project) {
            setSelectedProject(project);
          }
        }}
      >
        {projects.map((project) => (
          <MenuItem
            key={project.id}
            value={project.id}
          >
            {project.name}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}