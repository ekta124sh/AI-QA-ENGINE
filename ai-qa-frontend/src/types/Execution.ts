export interface ExecutionSummary {
  project_id: number;
  total_tests: number;
  passed: number;
  failed: number;
  status: string;
  last_execution: string | null;
}

export interface ExecutionHistory {
  execution_id: number;
  file_name: string;
  status: string;
  execution_time: string;
  report_path: string;
  created_at: string;
}