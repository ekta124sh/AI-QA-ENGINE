import AppRoutes from "./app/AppRoutes";
import { ProjectProvider } from "./context/ProjectContext";

function App() {
  return (
    <ProjectProvider>
      <AppRoutes />
    </ProjectProvider>
  );
}

export default App;