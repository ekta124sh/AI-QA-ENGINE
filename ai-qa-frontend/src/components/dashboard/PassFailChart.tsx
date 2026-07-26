import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import {
  Paper,
  Typography,
  Box,
  Stack,
  Chip,
} from "@mui/material";

interface Props {
  passed: number;
  failed: number;
}

const COLORS = ["#2e7d32", "#d32f2f"];

function PassFailChart({ passed, failed }: Props) {
  const total = passed + failed;

  const data = [
    { name: "Passed", value: passed },
    { name: "Failed", value: failed },
  ];

  const renderLabel = ({ percent }: any) =>
    `${(percent * 100).toFixed(0)}%`;

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
        Test Results Distribution
      </Typography>

      {total === 0 ? (
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          height="280px"
        >
          <Typography color="text.secondary">
            No execution data available
          </Typography>
        </Box>
      ) : (
        <>
          <ResponsiveContainer width="100%" height={240}>
            <PieChart>
              <Pie
                data={data}
                dataKey="value"
                nameKey="name"
                innerRadius={70}
                outerRadius={100}
                paddingAngle={3}
                label={renderLabel}
              >
                {data.map((entry, index) => (
                  <Cell
                    key={entry.name}
                    fill={COLORS[index]}
                  />
                ))}
              </Pie>

              <Tooltip
                formatter={(value: number) => [
                  value,
                  "Tests",
                ]}
              />
            </PieChart>
          </ResponsiveContainer>

          <Stack
            direction="row"
            spacing={2}
            justifyContent="center"
            mt={2}
          >
            <Chip
              label={`Passed : ${passed}`}
              color="success"
            />

            <Chip
              label={`Failed : ${failed}`}
              color="error"
            />
          </Stack>

          <Typography
            align="center"
            mt={2}
            color="text.secondary"
          >
            Total Executions : <strong>{total}</strong>
          </Typography>
        </>
      )}
    </Paper>
  );
}

export default PassFailChart;