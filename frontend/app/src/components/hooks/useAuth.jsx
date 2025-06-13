import { useEffect, useState } from "react";
import api from "../api";
import { ACCESS_TOKEN } from "../constants";

export function useAuth() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        await api.get("/auth/check");
        setIsAuthenticated(true);
      } catch {
        setIsAuthenticated(false);
        localStorage.removeItem(ACCESS_TOKEN);
      }
    };

    if (localStorage.getItem(ACCESS_TOKEN)) {
      checkAuth();
    }
  }, []);

  return isAuthenticated;
}
