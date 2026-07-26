import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
  is_active: boolean;
}

interface AuthState {
  token: string | null;
  user: User | null;
  isAuthenticated: boolean;
  loading: boolean;
}

const initialState: AuthState = {
  token: localStorage.getItem("token"),
  user: null,
  isAuthenticated: !!localStorage.getItem("token"),
  loading: false,
};

const authSlice = createSlice({
  name: "auth",

  initialState,

  reducers: {
    loginSuccess(
      state,
      action: PayloadAction<{
        token: string;
        user: User;
      }>
    ) {
      state.token = action.payload.token;
      state.user = action.payload.user;
      state.isAuthenticated = true;

      localStorage.setItem("token", action.payload.token);
    },

    logout(state) {
      state.token = null;
      state.user = null;
      state.isAuthenticated = false;

      localStorage.removeItem("token");
    },
  },
});

export const { loginSuccess, logout } = authSlice.actions;

export default authSlice.reducer;