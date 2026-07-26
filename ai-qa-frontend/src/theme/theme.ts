import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#1976d2",
    },

    secondary: {
      main: "#42a5f5",
    },

    background: {
      default: "#f4f7fb",
      paper: "#ffffff",
    },
  },

  shape: {
    borderRadius: 14,
  },

  typography: {
    fontFamily: "Inter, Roboto, sans-serif",

    h4: {
      fontWeight: 700,
    },

    h5: {
      fontWeight: 600,
    },

    h6: {
      fontWeight: 600,
    },
  },

  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          boxShadow: "0 8px 24px rgba(0,0,0,0.08)",
        },
      },
    },

    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 16,
        },
      },
    },
  },
});

export default theme;