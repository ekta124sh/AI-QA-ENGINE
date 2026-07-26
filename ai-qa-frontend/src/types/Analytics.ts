export interface PriorityDistribution {
  priority: string;
  count: number;
}

export interface SeverityDistribution {
  severity: string;
  count: number;
}

export interface TestTypeDistribution {
  test_type: string;
  count: number;
}

export interface ProjectDistribution {
  project: string;
  test_cases: number;
}