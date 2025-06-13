import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../Api";
import { ACCESS_TOKEN } from "../constants";

export function ProtectedRoute({ children }) {
  const navigate = useNavigate();

  useEffect(() => {
    const checkAuth = async () => {
      try {
        await api.get("/auth/check");
      } catch (error) {
        localStorage.removeItem(ACCESS_TOKEN);
        navigate("/login");
      }
    };

    if (!localStorage.getItem(ACCESS_TOKEN)) {
      navigate("/login");
    } else {
      checkAuth();
    }
  }, [navigate]);

  return localStorage.getItem(ACCESS_TOKEN) ? children : null;
}
