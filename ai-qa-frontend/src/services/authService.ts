import api from "../api/axios";

export interface LoginRequest {
  username: string;
  password: string;
}

export async function login(data: LoginRequest) {
  const formData = new URLSearchParams();

  formData.append("username", data.username);
  formData.append("password", data.password);

  const response = await api.post(
    "/auth/login",
    formData,
    {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    }
  );

  return response.data;
}