import { useEffect, useState } from "react";

import {
  Box,
  Chip,
  CircularProgress,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
  TextField,
  Button,
} from "@mui/material";

import type { TestCase } from "../../types/TestCase";

import { getTestCases } from "../../services/testcaseService";
import { useProject } from "../../context/ProjectContext";

import TestCaseDetailsDialog from "../../components/testcases/TestCaseDetailsDialog";

function TestCases() {
  const { selectedProject } = useProject();

  const [testCases, setTestCases] = useState<TestCase[]>([]);
  const [filteredCases, setFilteredCases] = useState<TestCase[]>([]);

  const [loading, setLoading] = useState(false);

  const [search, setSearch] = useState("");

  const [selectedTestCase, setSelectedTestCase] =
    useState<TestCase | null>(null);

  const [dialogOpen, setDialogOpen] = useState(false);

  useEffect(() => {
    if (selectedProject) {
      loadTestCases(selectedProject.id);
    }
  }, [selectedProject]);

  useEffect(() => {
    const filtered = testCases.filter(
      (tc) =>
        tc.title.toLowerCase().includes(search.toLowerCase()) ||
        tc.module.toLowerCase().includes(search.toLowerCase()) ||
        tc.test_type.toLowerCase().includes(search.toLowerCase())
    );

    setFilteredCases(filtered);
  }, [search, testCases]);

  const loadTestCases = async (projectId: number) => {
    try {
      setLoading(true);

      const data = await getTestCases(projectId);

      setTestCases(data);
      setFilteredCases(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  if (!selectedProject) {
    return (
      <Typography color="text.secondary">
        Please select a project.
      </Typography>
    );
  }

  return (
    <>
      <Typography variant="h4" fontWeight="bold" mb={1}>
        Test Cases
      </Typography>

      <Typography
        variant="subtitle1"
        color="text.secondary"
        mb={3}
      >
        Current Project:{" "}
        <strong>{selectedProject.name}</strong>
      </Typography>

      <Box
        sx={{
          display: "flex",
          gap: 2,
          mb: 3,
        }}
      >
        <TextField
          fullWidth
          label="Search Test Cases"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </Box>

      {loading ? (
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            mt: 6,
          }}
        >
          <CircularProgress />
        </Box>
      ) : (
        <TableContainer component={Paper}>
          <Table>

            <TableHead>
              <TableRow>
                <TableCell>ID</TableCell>
                <TableCell>Title</TableCell>
                <TableCell>Module</TableCell>
                <TableCell>Priority</TableCell>
                <TableCell>Severity</TableCell>
                <TableCell>Type</TableCell>
                <TableCell align="center">
                  Action
                </TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {filteredCases.map((tc) => (
                <TableRow hover key={tc.id}>
                  <TableCell>{tc.id}</TableCell>

                  <TableCell>{tc.title}</TableCell>

                  <TableCell>{tc.module}</TableCell>

                  <TableCell>
                    <Chip
                      label={tc.priority}
                      color={
                        tc.priority === "High"
                          ? "error"
                          : tc.priority === "Medium"
                          ? "warning"
                          : "success"
                      }
                    />
                  </TableCell>

                  <TableCell>
                    <Chip
                      label={tc.severity}
                      color={
                        tc.severity === "Critical"
                          ? "error"
                          : tc.severity === "Major"
                          ? "warning"
                          : "success"
                      }
                    />
                  </TableCell>

                  <TableCell>{tc.test_type}</TableCell>

                  <TableCell align="center">
                    <Button
                      variant="outlined"
                      size="small"
                      onClick={() => {
                        setSelectedTestCase(tc);
                        setDialogOpen(true);
                      }}
                    >
                      View
                    </Button>
                  </TableCell>
                </TableRow>
              ))}

              {!loading &&
                filteredCases.length === 0 && (
                  <TableRow>
                    <TableCell
                      colSpan={7}
                      align="center"
                    >
                      No Test Cases Found
                    </TableCell>
                  </TableRow>
                )}
            </TableBody>

          </Table>
        </TableContainer>
      )}

      <TestCaseDetailsDialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        testCase={selectedTestCase}
      />
    </>
  );
}

export default TestCases;