import {
  Box,
  Button,
  Card,
  CardContent,
  Container,
  IconButton,
  InputAdornment,
  Link,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

import { Visibility, VisibilityOff } from "@mui/icons-material";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

import AppSnackbar from "../../components/common/AppSnackbar";

function Login() {
  const [showPassword, setShowPassword] = useState(false);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success" as
      | "success"
      | "error"
      | "warning"
      | "info",
  });

  const navigate = useNavigate();

  const showSnackbar = (
    message: string,
    severity: "success" | "error" | "warning" | "info"
  ) => {
    setSnackbar({
      open: true,
      message,
      severity,
    });
  };

  const handleLogin = async () => {
    if (!email || !password) {
      showSnackbar(
        "Please enter your email and password.",
        "warning"
      );
      return;
    }

    try {
      setLoading(true);

      const formData = new URLSearchParams();

      formData.append("username", email);
      formData.append("password", password);

      const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded",
          },
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        showSnackbar(
          data.detail || "Invalid credentials",
          "error"
        );
        return;
      }

      localStorage.setItem(
        "token",
        data.access_token
      );

      const meResponse = await fetch(
        "http://127.0.0.1:8000/auth/me",
        {
          headers: {
            Authorization: `Bearer ${data.access_token}`,
          },
        }
      );

      const user = await meResponse.json();

      localStorage.setItem(
        "user",
        JSON.stringify(user)
      );

      showSnackbar(
        `Welcome ${user.name}!`,
        "success"
      );

      setTimeout(() => {
        navigate("/dashboard");
      }, 800);
    } catch (error) {
      console.error(error);

      showSnackbar(
        "Unable to connect to server.",
        "error"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Box
        sx={{
          minHeight: "100vh",
          bgcolor: "#f4f6f8",
          display: "flex",
          alignItems: "center",
        }}
      >
        <Container maxWidth="sm">
          <Card elevation={8}>
            <CardContent sx={{ p: 5 }}>
              <Stack spacing={3}>
                <Box textAlign="center">
                  <Typography
                    variant="h4"
                    fontWeight="bold"
                  >
                    AI QA Engine
                  </Typography>

                  <Typography
                    color="text.secondary"
                  >
                    Sign in to continue
                  </Typography>
                </Box>

                <TextField
                  fullWidth
                  label="Email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) =>
                    setEmail(e.target.value)
                  }
                />

                <TextField
                  fullWidth
                  label="Password"
                  type={
                    showPassword
                      ? "text"
                      : "password"
                  }
                  placeholder="Enter your password"
                  value={password}
                  onChange={(e) =>
                    setPassword(e.target.value)
                  }
                  InputProps={{
                    endAdornment: (
                      <InputAdornment position="end">
                        <IconButton
                          onClick={() =>
                            setShowPassword(
                              !showPassword
                            )
                          }
                        >
                          {showPassword ? (
                            <VisibilityOff />
                          ) : (
                            <Visibility />
                          )}
                        </IconButton>
                      </InputAdornment>
                    ),
                  }}
                />

                <Button
                  variant="contained"
                  size="large"
                  fullWidth
                  onClick={handleLogin}
                  disabled={loading}
                >
                  {loading
                    ? "Logging in..."
                    : "Login"}
                </Button>

                <Typography textAlign="center">
                  Don't have an account?{" "}
                  <Link href="/register">
                    Register
                  </Link>
                </Typography>
              </Stack>
            </CardContent>
          </Card>
        </Container>
      </Box>

      <AppSnackbar
        open={snackbar.open}
        message={snackbar.message}
        severity={snackbar.severity}
        onClose={() =>
          setSnackbar({
            ...snackbar,
            open: false,
          })
        }
      />
    </>
  );
}

export default Login;