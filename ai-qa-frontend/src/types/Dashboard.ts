export interface DashboardSummary {
  total_projects: number;
  total_manual_tests: number;
  total_playwright_tests: number;
  total_executions: number;
  total_passed: number;
  total_failed: number;
  overall_pass_rate: number;
}