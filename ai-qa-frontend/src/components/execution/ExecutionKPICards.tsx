import {
  Grid,
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import PlayArrowIcon from "@mui/icons-material/PlayArrow";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import PendingActionsIcon from "@mui/icons-material/PendingActions";

import type { ExecutionSummary } from "../../types/Execution";

interface Props {
  summary: ExecutionSummary;
}

export default function ExecutionKPICards({ summary }: Props) {
  const cards = [
    {
      title: "Total Tests",
      value: summary.total_tests,
      icon: <PlayArrowIcon color="primary" fontSize="large" />,
    },
    {
      title: "Passed",
      value: summary.passed,
      icon: <CheckCircleIcon color="success" fontSize="large" />,
    },
    {
      title: "Failed",
      value: summary.failed,
      icon: <CancelIcon color="error" fontSize="large" />,
    },
    {
      title: "Status",
      value: summary.status,
      icon: <PendingActionsIcon color="warning" fontSize="large" />,
    },
  ];

  return (
    <Grid container spacing={3}>
      {cards.map((card) => (
        <Grid item xs={12} sm={6} md={3} key={card.title}>
          <Card elevation={4}>
            <CardContent>
              <Typography
                variant="subtitle2"
                color="text.secondary"
              >
                {card.title}
              </Typography>

              <Typography
                variant="h4"
                fontWeight="bold"
                mt={1}
              >
                {card.value}
              </Typography>

              {card.icon}
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
}