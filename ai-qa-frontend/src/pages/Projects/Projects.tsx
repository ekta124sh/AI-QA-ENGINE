import { useEffect, useMemo, useState } from "react";

import {
  Box,
  Button,
  Chip,
  CircularProgress,
  InputAdornment,
  Link,
  Paper,
  Skeleton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TablePagination,
  TableRow,
  TextField,
  Typography,
} from "@mui/material";

import AddIcon from "@mui/icons-material/Add";
import PsychologyIcon from "@mui/icons-material/Psychology";
import SearchIcon from "@mui/icons-material/Search";
import GitHubIcon from "@mui/icons-material/GitHub";

import type { Project } from "../../types/Project";

import {
  getProjects,
  generateTests,
} from "../../services/projectService";

import CreateProjectDialog from "../../components/projects/CreateProjectDialog";

function Projects() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);

  const [dialogOpen, setDialogOpen] = useState(false);

  const [generatingId, setGeneratingId] =
    useState<number | null>(null);

  const [search, setSearch] = useState("");

  const [page, setPage] = useState(0);

  const [rowsPerPage, setRowsPerPage] = useState(5);

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      setLoading(true);

      const data = await getProjects();

      setProjects(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const filteredProjects = useMemo(() => {
    return projects.filter((project) => {
      const keyword = search.toLowerCase();

      return (
        project.name.toLowerCase().includes(keyword) ||
        project.description.toLowerCase().includes(keyword) ||
        (project.github_url ?? "")
          .toLowerCase()
          .includes(keyword)
      );
    });
  }, [projects, search]);

  const paginatedProjects = filteredProjects.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  const getStatusColor = (
    status: string
  ):
    | "primary"
    | "success"
    | "warning"
    | "error" => {
    switch (status) {
      case "NEW":
        return "primary";

      case "PROCESSING":
        return "warning";

      case "FAILED":
        return "error";

      default:
        return "success";
    }
  };

  const handleGenerateTests = async (
    projectId: number
  ) => {
    try {
      setGeneratingId(projectId);

      await generateTests(projectId);

      alert("Test cases generated successfully!");
    } catch (error) {
      console.error(error);

      alert("Failed to generate test cases.");
    } finally {
      setGeneratingId(null);
    }
  };

  return (
    <>
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          flexWrap: "wrap",
          gap: 2,
          mb: 3,
        }}
      >
        <Typography
          variant="h4"
          fontWeight={700}
        >
          Projects
        </Typography>

        <Box
          display="flex"
          gap={2}
        >
          <TextField
            size="small"
            placeholder="Search Projects..."
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              setPage(0);
            }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
          />

          <Button
            variant="contained"
            startIcon={<AddIcon />}
            onClick={() =>
              setDialogOpen(true)
            }
          >
            New Project
          </Button>
        </Box>
      </Box>

            <TableContainer
        component={Paper}
        sx={{
          borderRadius: 3,
          boxShadow: 3,
        }}
      >
        <Table>

          <TableHead
            sx={{
              backgroundColor: "#f5f7fa",
            }}
          >
            <TableRow>
              <TableCell><b>ID</b></TableCell>
              <TableCell><b>Name</b></TableCell>
              <TableCell><b>Description</b></TableCell>
              <TableCell><b>Repository</b></TableCell>
              <TableCell><b>Status</b></TableCell>
              <TableCell align="center">
                <b>Actions</b>
              </TableCell>
            </TableRow>
          </TableHead>

          <TableBody>

            {loading ? (

              [...Array(5)].map((_, index) => (

                <TableRow key={index}>

                  {[...Array(6)].map((_, i) => (

                    <TableCell key={i}>
                      <Skeleton
                        animation="wave"
                        height={35}
                      />
                    </TableCell>

                  ))}

                </TableRow>

              ))

            ) : paginatedProjects.length === 0 ? (

              <TableRow>

                <TableCell
                  colSpan={6}
                  align="center"
                >

                  <Box py={8}>

                    <Typography
                      variant="h6"
                      gutterBottom
                    >
                      No Projects Found
                    </Typography>

                    <Typography
                      color="text.secondary"
                    >
                      Create a new project or try another search.
                    </Typography>

                  </Box>

                </TableCell>

              </TableRow>

            ) : (

              paginatedProjects.map((project) => (

                <TableRow
                  hover
                  key={project.id}
                >

                  <TableCell>
                    {project.id}
                  </TableCell>

                  <TableCell>
                    <Typography
                      fontWeight={600}
                    >
                      {project.name}
                    </Typography>
                  </TableCell>

                  <TableCell>
                    {project.description}
                  </TableCell>

                  <TableCell>

                    {project.github_url ? (

                      <Link
                        href={project.github_url}
                        target="_blank"
                        underline="none"
                        display="flex"
                        alignItems="center"
                        gap={1}
                      >
                        <GitHubIcon
                          fontSize="small"
                        />
                        View Repository
                      </Link>

                    ) : (

                      "-"

                    )}

                  </TableCell>

                  <TableCell>

                    <Chip
                      label={project.status}
                      color={getStatusColor(
                        project.status
                      )}
                      size="small"
                    />

                  </TableCell>

                  <TableCell align="center">

                    <Button
                      variant="contained"
                      color="secondary"
                      size="small"
                      startIcon={
                        <PsychologyIcon />
                      }
                      disabled={
                        generatingId === project.id
                      }
                      onClick={() =>
                        handleGenerateTests(
                          project.id
                        )
                      }
                    >

                      {generatingId ===
                      project.id ? (
                        <CircularProgress
                          size={18}
                          color="inherit"
                        />
                      ) : (
                        "Generate Tests"
                      )}

                    </Button>

                  </TableCell>

                </TableRow>

              ))

            )}

          </TableBody>

        </Table>
      </TableContainer>

      <TablePagination
        component="div"
        count={filteredProjects.length}
        page={page}
        rowsPerPage={rowsPerPage}
        rowsPerPageOptions={[
          5,
          10,
          25,
        ]}
        onPageChange={(
          _,
          newPage
        ) => setPage(newPage)}
        onRowsPerPageChange={(
          event
        ) => {
          setRowsPerPage(
            parseInt(
              event.target.value,
              10
            )
          );
          setPage(0);
        }}
      />

      <CreateProjectDialog
        open={dialogOpen}
        onClose={() =>
          setDialogOpen(false)
        }
        onSuccess={loadProjects}
      />
    </>
  );
}

export default Projects;