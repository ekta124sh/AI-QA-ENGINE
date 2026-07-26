import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

import {
  Paper,
  Typography,
  Box,
  Chip,
} from "@mui/material";

const data = [
  { month: "Jan", executions: 12 },
  { month: "Feb", executions: 18 },
  { month: "Mar", executions: 25 },
  { month: "Apr", executions: 20 },
  { month: "May", executions: 28 },
  { month: "Jun", executions: 35 },
];

function ExecutionTrendChart() {
  const totalExecutions = data.reduce(
    (sum, item) => sum + item.executions,
    0
  );

  return (
    <Paper
      elevation={2}
      sx={{
        p: 3,
        borderRadius: 4,
        height: 380,
      }}
    >
      <Typography
        variant="h6"
        fontWeight={700}
        mb={3}
      >
        Monthly Execution Trend
      </Typography>

      <ResponsiveContainer width="100%" height={240}>
        <BarChart
          data={data}
          margin={{
            top: 10,
            right: 20,
            left: 0,
            bottom: 5,
          }}
        >
          <CartesianGrid
            strokeDasharray="3 3"
            vertical={false}
          />

          <XAxis
            dataKey="month"
            tickLine={false}
            axisLine={false}
          />

          <YAxis
            tickLine={false}
            axisLine={false}
          />

          <Tooltip
            cursor={{ fill: "#f5f7fb" }}
            formatter={(value: number) => [
              value,
              "Executions",
            ]}
          />

          <Bar
            dataKey="executions"
            fill="#1976d2"
            radius={[8, 8, 0, 0]}
            animationDuration={1200}
          />
        </BarChart>
      </ResponsiveContainer>

      <Box
        mt={3}
        display="flex"
        justifyContent="space-between"
        alignItems="center"
      >
        <Typography color="text.secondary">
          Total Executions
        </Typography>

        <Chip
          color="primary"
          label={totalExecutions}
        />
      </Box>
    </Paper>
  );
}

export default ExecutionTrendChart;