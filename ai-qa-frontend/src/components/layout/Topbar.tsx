import { useState } from "react";
import {
  AppBar,
  Avatar,
  Box,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  IconButton,
  Toolbar,
  Typography,
} from "@mui/material";

import {
  Notifications,
  Logout,
} from "@mui/icons-material";

import { useNavigate } from "react-router-dom";

import ProjectSelector from "../common/ProjectSelector";

function Topbar() {
  const navigate = useNavigate();

  const [logoutDialogOpen, setLogoutDialogOpen] = useState(false);

  const user = JSON.parse(
    localStorage.getItem("user") || "{}"
  );

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    localStorage.removeItem("selectedProject");

    navigate("/login");
  };

  return (
    <>
      <AppBar
        position="fixed"
        color="inherit"
        elevation={1}
        sx={{
          width: "calc(100% - 250px)",
          ml: "250px",
          borderBottom: "1px solid #e5e7eb",
        }}
      >
        <Toolbar
          sx={{
            display: "flex",
            justifyContent: "space-between",
            gap: 3,
          }}
        >
          {/* Left Side */}
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 3,
            }}
          >
            <Typography
              variant="h6"
              fontWeight="bold"
            >
              AI QA Engine
            </Typography>

            <ProjectSelector />
          </Box>

          {/* Right Side */}
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 2,
            }}
          >
            <IconButton>
              <Notifications />
            </IconButton>

            <Box
              sx={{
                display: "flex",
                alignItems: "center",
                gap: 1,
              }}
            >
              <Avatar sx={{ bgcolor: "#1976d2" }}>
                {user?.name?.charAt(0)?.toUpperCase() || "A"}
              </Avatar>

              <Box>
                <Typography fontWeight="bold">
                  {user?.name || "Guest"}
                </Typography>

                <Typography
                  variant="caption"
                  color="text.secondary"
                >
                  {user?.role || "User"}
                </Typography>
              </Box>
            </Box>

            <Button
              variant="outlined"
              color="error"
              startIcon={<Logout />}
              onClick={() => setLogoutDialogOpen(true)}
              sx={{
                ml: 2,
                borderRadius: 2,
                textTransform: "none",
              }}
            >
              Logout
            </Button>
          </Box>
        </Toolbar>
      </AppBar>

      {/* Logout Confirmation Dialog */}
      <Dialog
        open={logoutDialogOpen}
        onClose={() => setLogoutDialogOpen(false)}
        maxWidth="xs"
        fullWidth
      >
        <DialogTitle>🔒 Confirm Logout</DialogTitle>

        <DialogContent>
          <DialogContentText>
            Are you sure you want to log out from AI QA Engine?
          </DialogContentText>
        </DialogContent>

        <DialogActions sx={{ px: 3, pb: 3 }}>
          <Button
            onClick={() => setLogoutDialogOpen(false)}
            variant="outlined"
          >
            Cancel
          </Button>

          <Button
            color="error"
            variant="contained"
            onClick={handleLogout}
          >
            Logout
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default Topbar;