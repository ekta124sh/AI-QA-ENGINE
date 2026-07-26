import {
  createContext,
  useContext,
  useEffect,
  useState,
  ReactNode,
} from "react";

export interface Project {
  id: number;
  name: string;
  description: string;
  github_url: string;
  status: string;
}

interface ProjectContextType {
  projects: Project[];
  selectedProject: Project | null;
  setSelectedProject: (project: Project) => void;
  setProjects: (projects: Project[]) => void;
}

const ProjectContext = createContext<ProjectContextType | undefined>(undefined);

export function ProjectProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [projects, setProjects] = useState<Project[]>([]);
  const [selectedProject, setSelectedProject] =
    useState<Project | null>(null);

  useEffect(() => {
    const savedProject = localStorage.getItem("selectedProject");

    if (savedProject) {
      setSelectedProject(JSON.parse(savedProject));
    }
  }, []);

  useEffect(() => {
    if (selectedProject) {
      localStorage.setItem(
        "selectedProject",
        JSON.stringify(selectedProject)
      );
    }
  }, [selectedProject]);

  return (
    <ProjectContext.Provider
      value={{
        projects,
        selectedProject,
        setSelectedProject,
        setProjects,
      }}
    >
      {children}
    </ProjectContext.Provider>
  );
}

export function useProject() {
  const context = useContext(ProjectContext);

  if (!context) {
    throw new Error(
      "useProject must be used within ProjectProvider"
    );
  }

  return context;
}