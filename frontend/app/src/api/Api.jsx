import axios from "axios";
// import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// api.interceptors.request.use(
//   (config) => {
//     const token = localStorage.getItem(ACCESS_TOKEN);
//     if (token) {
//       config.headers.Authorization = `Bearer ${token}`;
//     }
//     return config;
//   },
//   (error) => {
//     return Promise.reject(error);
//   }
// );

// api.interceptors.response.use(
//   (response) => response,
//   (error) => {
//     if (error.response) {
//       const { status, data } = error.response;

//       let errorMessage = "Unknown error.";
//       if (data?.detail) {
//         errorMessage = data.detail;
//       }
//       alert(errorMessage);
//     } else {
//       alert(error);
//     }

//     return Promise.reject(error);
//   }
// );

export default api;
