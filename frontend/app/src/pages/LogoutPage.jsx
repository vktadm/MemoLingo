import { useEffect } from "react";
import { Container, Spinner } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { useAuth } from "../hooks/AuthContext";

export default function Logout() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    logout();
    navigate("/login", { replace: true });
  }, [navigate]);

  return (
    <Container className="m-5 text-center">
      <h3>Log out of the system...</h3>
      <Spinner as="span" animation="border" className="me-2"></Spinner>
    </Container>
  );
}
