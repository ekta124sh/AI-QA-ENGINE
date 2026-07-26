import { Grid } from "@mui/material";
import {
  Folder,
  Assignment,
  SmartToy,
  PlayArrow,
  CheckCircle,
  Cancel,
} from "@mui/icons-material";

import KPICard from "../common/KPICard";
import type { DashboardSummary } from "../../types/Dashboard";

interface DashboardCardsProps {
  summary: DashboardSummary;
}

export default function DashboardCards({
  summary,
}: DashboardCardsProps) {
  return (
    <Grid container spacing={3}>
      <Grid item xs={12} sm={6} md={4}>
        <KPICard
          title="Projects"
          value={summary.total_projects}
          icon={<Folder />}
        />
      </Grid>

      <Grid item xs={12} sm={6} md={4}>
        <KPICard
          title="Manual Tests"
          value={summary.total_manual_tests}
          icon={<Assignment />}
        />
      </Grid>

      <Grid item xs={12} sm={6} md={4}>
        <KPICard
          title="Playwright Tests"
          value={summary.total_playwright_tests}
          icon={<SmartToy />}
        />
      </Grid>

      <Grid item xs={12} sm={6} md={4}>
        <KPICard
          title="Executions"
          value={summary.total_executions}
          icon={<PlayArrow />}
        />
      </Grid>

      <Grid item xs={12} sm={6} md={4}>
        <KPICard
          title="Passed"
          value={summary.total_passed}
          icon={<CheckCircle />}
        />
      </Grid>

      <Grid item xs={12} sm={6} md={4}>
        <KPICard
          title="Failed"
          value={summary.total_failed}
          icon={<Cancel />}
        />
      </Grid>
    </Grid>
  );
}