import { createContext, useContext, useState } from "react";
import { ACCESS_TOKEN, CURRENT_USER } from "../constants";

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
          role: userData.role,
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
      // Здесь должен быть реальный вызов API
      await new Promise((resolve) => setTimeout(resolve, 1000));
      const mockUser = {
        id: 1,
        username: "Admin1",
        role: "admin",
        token: "mock-token",
      };
      setUser(mockUser);
      localStorage.setItem(ACCESS_TOKEN, mockUser.token);
      safeStoreUser(mockUser);
      return mockUser;
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem(ACCESS_TOKEN);
    safeRemoveUser();
  };

  const value = {
    user,
    isLoading,
    isLogin,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}
