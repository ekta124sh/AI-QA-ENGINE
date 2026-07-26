import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import Login from "../pages/Login/Login";
import Register from "../pages/Register/Register";
import Dashboard from "../pages/Dashboard/Dashboard";
import Projects from "../pages/Projects/Projects";
import TestCases from "../pages/TestCases/TestCases";
import PlaywrightScripts from "../pages/Playwright/PlaywrightScripts";
import Reports from "../pages/Reports/Reports";
import Executions from "../pages/Executions/Executions";
import Settings from "../pages/Settings/Settings";

import DashboardLayout from "../components/layout/DashboardLayout";
import ProtectedRoute from "../components/ProtectedRoute";
import NotFound from "../pages/NotFound/NotFound";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Default Route */}
        <Route path="/" element={<Navigate to="/login" replace />} />

        {/* Public Routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected Routes */}
        <Route
          element={
            <ProtectedRoute>
              <DashboardLayout />
            </ProtectedRoute>
          }
        >
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/testcases" element={<TestCases />} />
          <Route path="/playwright" element={<PlaywrightScripts />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/executions" element={<Executions />} />
          <Route path="/settings" element={<Settings />} />
        </Route>

        {/* 404 Page */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}