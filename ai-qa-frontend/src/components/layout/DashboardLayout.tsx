import { Box, Toolbar } from "@mui/material";
import { Outlet } from "react-router-dom";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

function DashboardLayout() {
  return (
    <Box sx={{ display: "flex" }}>

      <Sidebar />

      <Topbar />

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          ml: "250px",
        }}
      >
        <Toolbar />

        <Outlet />

      </Box>

    </Box>
  );
}

export default DashboardLayout;