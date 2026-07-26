import { useEffect, useState } from "react";
import {
  Box,
  Button,
  CircularProgress,
  Grid,
  Paper,
  Stack,
  Typography,
} from "@mui/material";

import AddCircleOutlinedIcon from "@mui/icons-material/AddCircleOutlined";
import FactCheckIcon from "@mui/icons-material/FactCheck";
import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import AssessmentIcon from "@mui/icons-material/Assessment";

import { useNavigate } from "react-router-dom";

import DashboardCards from "../../components/dashboard/DashboardCards";
import PassFailChart from "../../components/dashboard/PassFailChart";
import ExecutionTrendChart from "../../components/dashboard/ExecutionTrendChart";

import { getDashboardSummary } from "../../services/dashboardService";
import type { DashboardSummary } from "../../types/Dashboard";

import { useProject } from "../../context/ProjectContext";

function Dashboard() {
  const [summary, setSummary] = useState<DashboardSummary | null>(null);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  const { selectedProject } = useProject();

  const user = JSON.parse(localStorage.getItem("user") || "{}");

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        // Update this later if your backend supports project-wise dashboard
        const data = await getDashboardSummary();

        setSummary(data);
      } catch (error) {
        console.error("Failed to load dashboard:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  if (loading) {
    return (
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          mt: 8,
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  if (!summary) {
    return (
      <Typography color="error">
        Unable to load dashboard data.
      </Typography>
    );
  }

  return (
    <>
      {/* Hero Banner */}

      <Paper
        elevation={0}
        sx={{
          mb: 4,
          p: 4,
          borderRadius: 4,
          background:
            "linear-gradient(135deg,#1976d2 0%,#42a5f5 100%)",
          color: "white",
          overflow: "hidden",
        }}
      >
        <Typography variant="h4" fontWeight={700}>
          👋 Welcome back, {user?.name || "User"}
        </Typography>

        <Typography
          sx={{
            mt: 1,
            opacity: 0.95,
            maxWidth: 700,
            lineHeight: 1.8,
          }}
        >
          Manage your AI QA projects, generate intelligent
          test cases, create Playwright automation scripts,
          execute tests and analyse reports from one place.
        </Typography>

        {selectedProject && (
          <Typography
            sx={{
              mt: 3,
              fontWeight: 600,
              fontSize: "1rem",
            }}
          >
            📂 Current Project: {selectedProject.name}
          </Typography>
        )}

        <Stack
          direction="row"
          spacing={2}
          mt={4}
          flexWrap="wrap"
          useFlexGap
        >
          <Button
            variant="contained"
            color="inherit"
            startIcon={<AddCircleOutlinedIcon  />}
            onClick={() => navigate("/projects")}
          >
            Projects
          </Button>

          <Button
            variant="outlined"
            color="inherit"
            startIcon={<FactCheckIcon />}
            onClick={() => navigate("/testcases")}
            sx={{
              borderColor: "white",
              color: "white",
            }}
          >
            Test Cases
          </Button>

          <Button
            variant="outlined"
            color="inherit"
            startIcon={<PlayArrowIcon />}
            onClick={() => navigate("/playwright")}
            sx={{
              borderColor: "white",
              color: "white",
            }}
          >
            Playwright
          </Button>

          <Button
            variant="outlined"
            color="inherit"
            startIcon={<AssessmentIcon />}
            onClick={() => navigate("/reports")}
            sx={{
              borderColor: "white",
              color: "white",
            }}
          >
            Reports
          </Button>
        </Stack>
      </Paper>

      {/* KPI Cards */}

      <Box mb={4}>
        <DashboardCards summary={summary} />
      </Box>

      {/* Overall Pass Rate */}

      <Paper
        elevation={2}
        sx={{
          p: 4,
          borderRadius: 4,
          textAlign: "center",
          mb: 4,
        }}
      >
        <Typography
          variant="h5"
          fontWeight={600}
          color="text.secondary"
        >
          Overall Pass Rate
        </Typography>

        <Typography
          variant="h2"
          fontWeight={700}
          mt={2}
          color={
            summary.overall_pass_rate >= 80
              ? "success.main"
              : summary.overall_pass_rate >= 50
              ? "warning.main"
              : "error.main"
          }
        >
          {summary.overall_pass_rate}%
        </Typography>
      </Paper>

      {/* Charts */}

      <Grid container spacing={3}>
        <Grid item xs={12} lg={7}>
          <PassFailChart
            passed={summary.total_passed}
            failed={summary.total_failed}
          />
        </Grid>

        <Grid item xs={12} lg={5}>
          <ExecutionTrendChart />
        </Grid>
      </Grid>
    </>
  );
}

export default Dashboard;