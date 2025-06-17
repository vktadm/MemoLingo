import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => {
    // Успешные ответы (2xx)
    console.log({
      success: true,
      data: response.data,
      status: response.status,
    });

    return {
      success: true,
      data: response.data,
      status: response.status,
    };
  },
  (error) => {
    if (error.response) {
      // Ответы с ошибкой сервера
      const status = error.response.status;
      const data = error.response.data;

      const errorResponse = {
        success: false,
        status,
        message: data?.detail || "Uncnown error.",
      };

      console.log(errorResponse);

      return Promise.reject(errorResponse);
    } else if (error.request) {
      // Запрос был сделан, но ответ не получен
      return Promise.reject({
        success: false,
        message: "Couldn't get a response from the server.",
      });
    } else {
      // Ошибка при настройке запроса
      return Promise.reject({
        success: false,
        message: "Error when sending the request.",
      });
    }
  }
);

export default api;
