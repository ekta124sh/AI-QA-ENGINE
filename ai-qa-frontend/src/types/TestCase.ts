export interface TestCase {
  id: number;
  project_id: number;
  file_name: string;
  chunk_number: number;
  title: string;
  module: string;
  priority: string;
  severity: string;
  test_type: string;
  preconditions: string;
  steps: string[];
  expected_result: string;
}