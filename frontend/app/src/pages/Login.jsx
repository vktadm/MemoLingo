import { Col, Container, Row } from "react-bootstrap";
import UserForm from "../components/Form";
import { LogoCommon } from "../components/Logo";

import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../Api";
import { ACCESS_TOKEN } from "../constants";

function Login() {
  const navigate = useNavigate();

  useEffect(() => {
    const checkAuth = async () => {
      try {
        await api.get("/auth/check");
        navigate("/");
      } catch {}
    };

    if (localStorage.getItem(ACCESS_TOKEN)) {
      checkAuth();
    }
  }, [navigate]);

  return (
    <Container fluid>
      <Row className="align-items-center justify-content-center">
        <Col xs={12} sm={10} md={10} lg={8} xl={6} className="text-center">
          <div className="my-5">
            <LogoCommon className="text-center" />
          </div>
          <UserForm route="/auth/login" method="login" />
        </Col>
      </Row>
    </Container>
  );
}

export default Login;
