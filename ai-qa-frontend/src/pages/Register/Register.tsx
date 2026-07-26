import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  Stack,
  TextField,
  Typography,
  Link,
  Snackbar,
  Alert,
} from "@mui/material";

import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const navigate = useNavigate();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success" as "success" | "error",
  });

  const showMessage = (
    message: string,
    severity: "success" | "error"
  ) => {
    setSnackbar({
      open: true,
      message,
      severity,
    });
  };

  const handleRegister = async () => {
    if (!name || !email || !password) {
      showMessage("Please fill all fields.", "error");
      return;
    }

    if (password !== confirmPassword) {
      showMessage("Passwords do not match.", "error");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/auth/register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name,
            email,
            password,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        showMessage(data.detail, "error");
        return;
      }

      showMessage(
        "Registration Successful!",
        "success"
      );

      setTimeout(() => {
        navigate("/login");
      }, 1500);
    } catch {
      showMessage(
        "Unable to connect to server.",
        "error"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        bgcolor: "#f4f6f8",
      }}
    >
      <Container maxWidth="sm">
        <Card elevation={8}>
          <CardContent sx={{ p: 5 }}>
            <Stack spacing={3}>

              <Typography
                variant="h4"
                fontWeight="bold"
                textAlign="center"
              >
                Create Account
              </Typography>

              <TextField
                label="Full Name"
                value={name}
                onChange={(e) =>
                  setName(e.target.value)
                }
                fullWidth
              />

              <TextField
                label="Email"
                value={email}
                onChange={(e) =>
                  setEmail(e.target.value)
                }
                fullWidth
              />

              <TextField
                label="Password"
                type="password"
                value={password}
                onChange={(e) =>
                  setPassword(e.target.value)
                }
                fullWidth
              />

              <TextField
                label="Confirm Password"
                type="password"
                value={confirmPassword}
                onChange={(e) =>
                  setConfirmPassword(e.target.value)
                }
                fullWidth
              />

              <Button
                variant="contained"
                size="large"
                onClick={handleRegister}
                disabled={loading}
              >
                {loading
                  ? "Creating Account..."
                  : "Register"}
              </Button>

              <Typography textAlign="center">
                Already have an account?{" "}
                <Link href="/login">
                  Login
                </Link>
              </Typography>

            </Stack>
          </CardContent>
        </Card>
      </Container>

      <Snackbar
        open={snackbar.open}
        autoHideDuration={3000}
        onClose={() =>
          setSnackbar({
            ...snackbar,
            open: false,
          })
        }
      >
        <Alert severity={snackbar.severity}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Box>
  );
}