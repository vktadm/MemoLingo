import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import api from "../Api";
import { ACCESS_TOKEN } from "../constants";
import { LoadingSpinner } from "./LoadingSpinner";

export function NoAuthRoute({ children }) {
  const navigate = useNavigate();
  const [isCheckingAuth, setIsCheckingAuth] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (!token) {
          setIsCheckingAuth(false);
          return;
        }

        await api.get("/auth/check");
        navigate("/", { replace: true });
      } catch (error) {
        console.error("Auth check failed:", error);
        localStorage.removeItem(ACCESS_TOKEN);
        setIsCheckingAuth(false);
        navigate("/login", { replace: true });
      }
    };

    checkAuth();
  }, [navigate]);

  if (isCheckingAuth) {
    return (
      <Container>
        <LoadingSpinner />
      </Container>
    );
  }

  return !localStorage.getItem(ACCESS_TOKEN) ? children : null;
}
