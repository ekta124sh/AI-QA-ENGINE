import { useState } from "react";
import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
} from "@mui/material";

import { createProject } from "../../services/projectService";

interface Props {
  open: boolean;
  onClose: () => void;
  onSuccess: () => void;
}

function CreateProjectDialog({
  open,
  onClose,
  onSuccess,
}: Props) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [githubUrl, setGithubUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleCreate = async () => {
    try {
      setLoading(true);

      await createProject({
        name,
        description,
        github_url: githubUrl,
      });

      setName("");
      setDescription("");
      setGithubUrl("");

      onSuccess();
      onClose();
    } catch (err) {
      console.error(err);
      alert("Failed to create project");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Dialog
      open={open}
      onClose={onClose}
      fullWidth
      maxWidth="sm"
    >
      <DialogTitle>Create New Project</DialogTitle>

      <DialogContent>
        <TextField
          fullWidth
          label="Project Name"
          margin="normal"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <TextField
          fullWidth
          label="Description"
          margin="normal"
          multiline
          rows={3}
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <TextField
          fullWidth
          label="GitHub Repository URL"
          margin="normal"
          value={githubUrl}
          onChange={(e) => setGithubUrl(e.target.value)}
        />
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose}>
          Cancel
        </Button>

        <Button
          variant="contained"
          onClick={handleCreate}
          disabled={loading}
        >
          {loading ? "Creating..." : "Create Project"}
        </Button>
      </DialogActions>
    </Dialog>
  );
}

export default CreateProjectDialog;