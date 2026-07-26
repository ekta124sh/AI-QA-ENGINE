import { Card, CardContent, Typography, Box } from "@mui/material";
import type { ReactNode } from "react";

interface KPICardProps {
  title: string;
  value: string | number;
  icon: ReactNode;
}

function KPICard({ title, value, icon }: KPICardProps) {
  return (
    <Card
      elevation={0}
      sx={{
        height: "100%",
        borderRadius: 4,
        border: "1px solid",
        borderColor: "divider",
        background:
          "linear-gradient(135deg, #ffffff 0%, #f8fbff 100%)",
        transition: "all 0.3s ease",

        "&:hover": {
          transform: "translateY(-6px)",
          boxShadow: "0 12px 30px rgba(25,118,210,0.15)",
          borderColor: "primary.main",
        },
      }}
    >
      <CardContent sx={{ p: 3 }}>
        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="flex-start"
        >
          <Box flex={1}>
            <Typography
              variant="body2"
              color="text.secondary"
              fontWeight={600}
              sx={{ letterSpacing: 0.5 }}
            >
              {title.toUpperCase()}
            </Typography>

            <Typography
              variant="h3"
              fontWeight={700}
              mt={2}
              color="text.primary"
            >
              {value}
            </Typography>

            <Typography
              variant="caption"
              color="text.secondary"
              mt={1}
              display="block"
            >
              Updated just now
            </Typography>
          </Box>

          <Box
            sx={{
              width: 64,
              height: 64,
              borderRadius: "50%",
              background:
                "linear-gradient(135deg, #1976d2 0%, #42a5f5 100%)",
              color: "#fff",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              boxShadow: "0 8px 20px rgba(25,118,210,0.35)",

              "& svg": {
                fontSize: 32,
              },
            }}
          >
            {icon}
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
}

export default KPICard;