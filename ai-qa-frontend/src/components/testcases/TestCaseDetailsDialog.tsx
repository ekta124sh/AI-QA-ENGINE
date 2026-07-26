import { useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Typography,
  Chip,
  Stack,
  Divider,
  Button,
  CircularProgress,
  Snackbar,
  Alert,
  Box,
} from "@mui/material";

import type { TestCase } from "../../types/TestCase";
import { generatePlaywright } from "../../services/playwrightService";

interface Props {
  open: boolean;
  onClose: () => void;
  testCase: TestCase | null;
}

function TestCaseDetailsDialog({
  open,
  onClose,
  testCase,
}: Props) {
  const navigate = useNavigate();

  const [loading, setLoading] = useState(false);

  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [severity, setSeverity] = useState<"success" | "error">("success");

  if (!testCase) return null;

  const handleGeneratePlaywright = async () => {
    try {
      setLoading(true);

      const response = await generatePlaywright(testCase.project_id);

      setSeverity("success");
      setSnackbarMessage(response.message);
      setSnackbarOpen(true);

      setTimeout(() => {
        onClose();
        navigate("/playwright");
      }, 1000);
    } catch (error) {
      console.error(error);

      setSeverity("error");
      setSnackbarMessage("Failed to generate Playwright scripts.");
      setSnackbarOpen(true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Dialog
        open={open}
        onClose={onClose}
        maxWidth="lg"
        fullWidth
        PaperProps={{
          sx: {
            borderRadius: 3,
            minHeight: 650,
          },
        }}
      >
        <DialogTitle
          sx={{
            bgcolor: "primary.main",
            color: "white",
            fontWeight: 700,
            fontSize: 24,
          }}
        >
          {testCase.title}
        </DialogTitle>

        <DialogContent dividers sx={{ p: 4 }}>
          <Stack direction="row" spacing={2} mb={3}>
            <Chip
              label={testCase.priority}
              color="primary"
              sx={{ fontWeight: 600 }}
            />

            <Chip
              label={testCase.severity}
              color="error"
              sx={{ fontWeight: 600 }}
            />

            <Chip
              label={testCase.test_type}
              color="success"
              sx={{ fontWeight: 600 }}
            />
          </Stack>

          <Box mb={3}>
            <Typography
              variant="subtitle1"
              fontWeight="bold"
              color="primary"
              gutterBottom
            >
              📁 Module
            </Typography>

            <Typography>{testCase.module}</Typography>
          </Box>

          <Divider sx={{ my: 2 }} />

          <Box mb={3}>
            <Typography
              variant="subtitle1"
              fontWeight="bold"
              color="primary"
              gutterBottom
            >
              📋 Preconditions
            </Typography>

            <Typography>{testCase.preconditions}</Typography>
          </Box>

          <Divider sx={{ my: 2 }} />

          <Box mb={3}>
            <Typography
              variant="subtitle1"
              fontWeight="bold"
              color="primary"
              gutterBottom
            >
              📝 Test Steps
            </Typography>

            <Box
              sx={{
                bgcolor: "#f8f9fa",
                p: 2,
                borderRadius: 2,
                maxHeight: 220,
                overflowY: "auto",
              }}
            >
              <ol style={{ margin: 0, paddingLeft: 20 }}>
                {testCase.steps.map((step, index) => (
                  <li key={index}>
                    <Typography sx={{ mb: 1 }}>
                      {step}
                    </Typography>
                  </li>
                ))}
              </ol>
            </Box>
          </Box>

          <Divider sx={{ my: 2 }} />

          <Box>
            <Typography
              variant="subtitle1"
              fontWeight="bold"
              color="primary"
              gutterBottom
            >
              ✅ Expected Result
            </Typography>

            <Typography>{testCase.expected_result}</Typography>
          </Box>
        </DialogContent>

        <DialogActions
          sx={{
            px: 3,
            py: 2,
            borderTop: "1px solid #eee",
          }}
        >
          <Button
            variant="outlined"
            onClick={onClose}
          >
            Close
          </Button>

          <Button
            variant="contained"
            color="secondary"
            onClick={handleGeneratePlaywright}
            disabled={loading}
            startIcon={
              loading ? (
                <CircularProgress
                  size={18}
                  color="inherit"
                />
              ) : null
            }
          >
            {loading
              ? "Generating..."
              : "Generate Playwright Script"}
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar
        open={snackbarOpen}
        autoHideDuration={3000}
        onClose={() => setSnackbarOpen(false)}
        anchorOrigin={{
          vertical: "bottom",
          horizontal: "right",
        }}
      >
        <Alert
          severity={severity}
          variant="filled"
          sx={{ width: "100%" }}
        >
          {snackbarMessage}
        </Alert>
      </Snackbar>
    </>
  );
}

export default TestCaseDetailsDialog;