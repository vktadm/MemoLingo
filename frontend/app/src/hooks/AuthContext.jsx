import { createContext, useContext, useEffect, useState } from "react";
import api from "../Api";
import {
  ACCESS_TOKEN,
  CURRENT_USER,
  LOGIN_ROUTE,
  LOGOUT_ROUTE,
  REGISTER_ROUTE,
} from "../constants";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [isLoading, setIsLoading] = useState(false);
  const [user, setUser] = useState(() => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    const storedUser = localStorage.getItem(CURRENT_USER);

    return token && storedUser ? JSON.parse(storedUser) : null;
  });

  const isLogin = !!user && !!localStorage.getItem(ACCESS_TOKEN);
  const safeStoreUser = (userData) => {
    try {
      localStorage.setItem(
        CURRENT_USER,
        JSON.stringify({
          id: userData.id,
          username: userData.username,
          role: userData.user_role,
        })
      );
    } catch (e) {
      console.error("Failed to store user data", e);
    }
  };
  const safeRemoveUser = () => {
    try {
      localStorage.removeItem(CURRENT_USER);
    } catch (e) {
      console.error("Failed to remove user data", e);
    }
  };

  const login = async (credentials) => {
    setIsLoading(true);
    try {
      const response = await api.post(LOGIN_ROUTE, credentials);
      const user_data = response.data;

      setUser(user_data);
      localStorage.setItem(ACCESS_TOKEN, response.data.access_token);
      safeStoreUser(user_data);

      return response;
    } catch (error) {
      return error;
    } finally {
      setIsLoading(false);
    }
  };

  const logout = async () => {
    try {
      const response = await api.post(LOGOUT_ROUTE);
      return response;
    } catch (error) {
      return error;
    } finally {
      setUser(null);
      localStorage.removeItem(ACCESS_TOKEN);
      safeRemoveUser();
    }
  };

  const register = async (credentials) => {
    setIsLoading(true);
    try {
      const response = await api.post(REGISTER_ROUTE, credentials);
      return response;
    } catch (error) {
      return error;
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token && !user) {
      // Можно добавить проверку токена через API
      const storedUser = localStorage.getItem(CURRENT_USER);
      if (storedUser) setUser(JSON.parse(storedUser));
    }
  }, []);

  const value = {
    user,
    isLoading,
    isLogin,
    login,
    logout,
    register,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}
