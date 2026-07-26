import {
  Box,
  Button,
  Container,
  Paper,
  Typography,
} from "@mui/material";
import ReportProblemOutlinedIcon from "@mui/icons-material/ReportProblemOutlined";
import HomeIcon from "@mui/icons-material/Home";
import { useNavigate } from "react-router-dom";

export default function NotFound() {
  const navigate = useNavigate();

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          minHeight: "80vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Paper
          elevation={6}
          sx={{
            p: 6,
            borderRadius: 4,
            textAlign: "center",
            width: "100%",
          }}
        >
          <ReportProblemOutlinedIcon
  color="primary"
  sx={{
    fontSize: 80,
    mb: 2,
  }}
/>

          <Typography
            variant="h2"
            fontWeight="bold"
            color="primary"
          >
            404
          </Typography>

          <Typography
            variant="h5"
            mt={2}
            fontWeight={600}
          >
            Oops! Page Not Found
          </Typography>

          <Typography
            color="text.secondary"
            mt={2}
            mb={4}
          >
            The page you are looking for doesn't exist,
            has been moved, or the URL is incorrect.
          </Typography>

          <Button
            variant="contained"
            size="large"
            startIcon={<HomeIcon />}
            onClick={() => navigate("/dashboard")}
          >
            Back to Dashboard
          </Button>
        </Paper>
      </Box>
    </Container>
  );
}