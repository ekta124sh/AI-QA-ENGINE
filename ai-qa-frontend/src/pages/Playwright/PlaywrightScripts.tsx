import { useEffect, useState } from "react";

import {
  Box,
  Typography,
  CircularProgress,
  Paper,
  List,
  ListItemButton,
  ListItemText,
  Divider,
  TextField,
  InputAdornment,
  Button,
  Snackbar,
  Alert,
} from "@mui/material";

import SearchIcon from "@mui/icons-material/Search";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";

import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

import type { PlaywrightScript } from "../../types/Playwright";
import { getPlaywrightScripts } from "../../services/playwrightService";
import { useProject } from "../../context/ProjectContext";

function PlaywrightScripts() {
  const { selectedProject } = useProject();

  const [scripts, setScripts] = useState<PlaywrightScript[]>([]);
  const [filteredScripts, setFilteredScripts] = useState<PlaywrightScript[]>([]);
  const [selectedScript, setSelectedScript] =
    useState<PlaywrightScript | null>(null);

  const [loading, setLoading] = useState(false);
  const [search, setSearch] = useState("");

  const [copied, setCopied] = useState(false);

  useEffect(() => {
    if (selectedProject) {
      loadScripts(selectedProject.id);
    }
  }, [selectedProject]);

  useEffect(() => {
    const filtered = scripts.filter((script) =>
      script.file_name.toLowerCase().includes(search.toLowerCase())
    );

    setFilteredScripts(filtered);
  }, [search, scripts]);

  const loadScripts = async (projectId: number) => {
    try {
      setLoading(true);

      const data = await getPlaywrightScripts(projectId);

      setScripts(data);
      setFilteredScripts(data);

      if (data.length > 0) {
        setSelectedScript(data[0]);
      } else {
        setSelectedScript(null);
      }
    } finally {
      setLoading(false);
    }
  };

  const copyScript = () => {
    if (!selectedScript) return;

    navigator.clipboard.writeText(selectedScript.script);
    setCopied(true);
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
        🎭 Playwright Script Explorer
      </Typography>

      <Typography
        variant="subtitle1"
        color="text.secondary"
        mb={3}
      >
        Current Project: <strong>{selectedProject.name}</strong>
      </Typography>

      <TextField
        fullWidth
        label="Search Script"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        sx={{ mb: 3 }}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }}
      />

      {loading ? (
        <Box
          display="flex"
          justifyContent="center"
          mt={6}
        >
          <CircularProgress />
        </Box>
      ) : (
        <Box display="flex" gap={3}>
          <Paper
            elevation={3}
            sx={{
              width: 380,
              borderRadius: 3,
              height: "75vh",
              overflow: "auto",
            }}
          >
            <List>
              {filteredScripts.map((script) => (
                <Box key={script.id}>
                  <ListItemButton
                    selected={selectedScript?.id === script.id}
                    onClick={() => setSelectedScript(script)}
                    sx={{
                      borderRadius: 2,
                      m: 1,
                      "&.Mui-selected": {
                        bgcolor: "#E3F2FD",
                      },
                    }}
                  >
                    <ListItemText
                      primary={script.file_name}
                      secondary={`Chunk #${script.chunk_number}`}
                    />
                  </ListItemButton>

                  <Divider />
                </Box>
              ))}
            </List>
          </Paper>

          <Paper
            elevation={3}
            sx={{
              flex: 1,
              borderRadius: 3,
              p: 3,
              height: "75vh",
              overflow: "auto",
            }}
          >
            {selectedScript ? (
              <>
                <Box
                  display="flex"
                  justifyContent="space-between"
                  alignItems="center"
                  mb={2}
                >
                  <Typography
                    variant="h6"
                    fontWeight="bold"
                  >
                    {selectedScript.file_name}
                  </Typography>

                  <Button
                    variant="contained"
                    startIcon={<ContentCopyIcon />}
                    onClick={copyScript}
                  >
                    Copy Script
                  </Button>
                </Box>

                <SyntaxHighlighter
                  language="typescript"
                  style={oneDark}
                  showLineNumbers
                  wrapLongLines
                  customStyle={{
                    borderRadius: 12,
                    fontSize: 14,
                  }}
                >
                  {selectedScript.script}
                </SyntaxHighlighter>
              </>
            ) : (
              <Typography color="text.secondary">
                No Playwright script available for this project.
              </Typography>
            )}
          </Paper>
        </Box>
      )}

      <Snackbar
        open={copied}
        autoHideDuration={2500}
        onClose={() => setCopied(false)}
        anchorOrigin={{
          vertical: "bottom",
          horizontal: "right",
        }}
      >
        <Alert
          severity="success"
          variant="filled"
        >
          Script copied to clipboard!
        </Alert>
      </Snackbar>
    </>
  );
}

export default PlaywrightScripts;