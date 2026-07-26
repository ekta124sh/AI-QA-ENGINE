import { useEffect, useState } from "react";

import {
  Alert,
  Box,
  Button,
  CircularProgress,
  Stack,
  Typography,
} from "@mui/material";

import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import RefreshIcon from "@mui/icons-material/Refresh";

import ExecutionKPICards from "../../components/execution/ExecutionKPICards";
import ExecutionHistoryTable from "../../components/execution/ExecutionHistoryTable";

import {
  executeProject,
  getExecutionHistory,
  getExecutionSummary,
} from "../../services/executionService";

import type {
  ExecutionSummary,
  ExecutionHistory,
} from "../../types/Execution";

import { useProject } from "../../context/ProjectContext";

export default function Executions() {
  const { selectedProject } = useProject();

  const [summary, setSummary] =
    useState<ExecutionSummary | null>(null);

  const [history, setHistory] =
    useState<ExecutionHistory[]>([]);

  const [loading, setLoading] =
    useState(true);

  const [executing, setExecuting] =
    useState(false);

  const [error, setError] =
    useState("");

  useEffect(() => {
    if (selectedProject) {
      loadExecutionData();
    }
  }, [selectedProject]);

  const loadExecutionData = async () => {
    if (!selectedProject) return;

    try {
      setLoading(true);

      const [
        summaryResponse,
        historyResponse,
      ] = await Promise.all([
        getExecutionSummary(selectedProject.id),
        getExecutionHistory(selectedProject.id),
      ]);

      setSummary(summaryResponse);
      setHistory(historyResponse);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Failed to load execution data.");
    } finally {
      setLoading(false);
    }
  };

  const handleExecute = async () => {
    if (!selectedProject) return;

    try {
      setExecuting(true);

      await executeProject(selectedProject.id);

      await loadExecutionData();
    } catch (err) {
      console.error(err);
      alert("Execution failed.");
    } finally {
      setExecuting(false);
    }
  };

  if (!selectedProject) {
    return (
      <Alert severity="info">
        Please select a project.
      </Alert>
    );
  }

  if (loading) {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        height="60vh"
      >
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return (
      <Alert severity="error">
        {error}
      </Alert>
    );
  }

  if (!summary) {
    return (
      <Alert severity="warning">
        No execution data found.
      </Alert>
    );
  }

  return (
    <Box sx={{ p: 3 }}>
      <Typography
        variant="h4"
        fontWeight="bold"
        mb={3}
      >
        Execution Dashboard
      </Typography>

      <Typography
        variant="subtitle1"
        color="text.secondary"
        mb={2}
      >
        Current Project: <strong>{selectedProject.name}</strong>
      </Typography>

      <Stack
        direction="row"
        spacing={2}
        mb={3}
      >
        <Button
          variant="contained"
          startIcon={<PlayArrowIcon />}
          onClick={handleExecute}
          disabled={executing}
        >
          {executing
            ? "Executing..."
            : "Run Playwright Tests"}
        </Button>

        <Button
          variant="outlined"
          startIcon={<RefreshIcon />}
          onClick={loadExecutionData}
        >
          Refresh
        </Button>
      </Stack>

      <ExecutionKPICards summary={summary} />

      <Box mt={4}>
        <ExecutionHistoryTable
          history={history}
        />
      </Box>
    </Box>
  );
}