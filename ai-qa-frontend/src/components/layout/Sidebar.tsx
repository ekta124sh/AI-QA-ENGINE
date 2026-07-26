import {
  Box,
  Divider,
  Drawer,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";

import {
  Dashboard,
  Folder,
  Description,
  Code,
  Assessment,
  PlayCircleFilled,
  Settings,
  Logout,
} from "@mui/icons-material";

import { Link, useLocation } from "react-router-dom";

const drawerWidth = 250;

const menuItems = [
  {
    text: "Dashboard",
    icon: <Dashboard />,
    path: "/dashboard",
  },
  {
    text: "Projects",
    icon: <Folder />,
    path: "/projects",
  },
  {
    text: "Test Cases",
    icon: <Description />,
    path: "/testcases",
  },
  {
    text: "Playwright Scripts",
    icon: <Code />,
    path: "/playwright",
  },
  {
    text: "Reports",
    icon: <Assessment />,
    path: "/reports",
  },
  {
    text: "Executions",
    icon: <PlayCircleFilled />,
    path: "/executions",
  },
  {
    text: "Settings",
    icon: <Settings />,
    path: "/settings",
  },
];

function Sidebar() {
  const location = useLocation();

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: drawerWidth,
          boxSizing: "border-box",
        },
      }}
    >
      <Toolbar>
        <Typography
          variant="h6"
          fontWeight="bold"
        >
          AI QA Engine
        </Typography>
      </Toolbar>

      <Divider />

      <List>
        {menuItems.map((item) => (
          <ListItemButton
            key={item.text}
            component={Link}
            to={item.path}
            selected={location.pathname === item.path}
          >
            <ListItemIcon>{item.icon}</ListItemIcon>

            <ListItemText primary={item.text} />
          </ListItemButton>
        ))}
      </List>

      <Box sx={{ flexGrow: 1 }} />

      <Divider />

      <List>
        <ListItemButton>
          <ListItemIcon>
            <Logout color="error" />
          </ListItemIcon>

          <ListItemText primary="Logout" />
        </ListItemButton>
      </List>
    </Drawer>
  );
}

export default Sidebar;