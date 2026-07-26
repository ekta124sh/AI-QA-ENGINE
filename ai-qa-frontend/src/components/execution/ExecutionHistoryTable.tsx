import {
  Card,
  CardContent,
  Typography,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  Chip,
  TableContainer,
} from "@mui/material";

import type { ExecutionHistory } from "../../types/Execution";

interface Props {
  history: ExecutionHistory[];
}

export default function ExecutionHistoryTable({
  history,
}: Props) {
  return (
    <Card elevation={4}>
      <CardContent>

        <Typography
          variant="h6"
          fontWeight="bold"
          mb={2}
        >
          Execution History
        </Typography>

        <TableContainer>

          <Table>

            <TableHead>

              <TableRow>

                <TableCell>
                  <b>File Name</b>
                </TableCell>

                <TableCell>
                  <b>Status</b>
                </TableCell>

                <TableCell>
                  <b>Execution Time</b>
                </TableCell>

                <TableCell>
                  <b>Executed At</b>
                </TableCell>

              </TableRow>

            </TableHead>

            <TableBody>

              {history.map((item) => (
                <TableRow key={item.execution_id}>

                  <TableCell>
                    {item.file_name}
                  </TableCell>

                  <TableCell>

                    <Chip
                      label={item.status}
                      color={
                        item.status === "PASS"
                          ? "success"
                          : "error"
                      }
                    />

                  </TableCell>

                  <TableCell>
                    {item.execution_time}
                  </TableCell>

                  <TableCell>
                    {item.created_at}
                  </TableCell>

                </TableRow>
              ))}

            </TableBody>

          </Table>

        </TableContainer>

      </CardContent>
    </Card>
  );
}