import { ReactNode } from "react";

import { Provider } from "react-redux";

import { ThemeProvider } from "@mui/material/styles";

import CssBaseline from "@mui/material/CssBaseline";

import { Toaster } from "react-hot-toast";

import theme from "../theme/theme";

import { store } from "../store/store";

interface Props {
  children: ReactNode;
}

function Providers({ children }: Props) {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <CssBaseline />

        {children}

        <Toaster position="top-right" />
      </ThemeProvider>
    </Provider>
  );
}

export default Providers;