import { useEffect } from "react";
import { Col, Container, Row, Spinner } from "react-bootstrap";
import { useLocation, useNavigate } from "react-router-dom";
import api from "../Api";
import { LogoCommon } from "../components/Logo";
import { ACCESS_TOKEN } from "../constants";

const GoogleAuthCallback = () => {
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    const handleGoogleCallback = async () => {
      try {
        const searchParams = new URLSearchParams(location.search);
        console.log(searchParams);
        const authCode = searchParams.get("code");
        const error = searchParams.get("error");

        if (error) {
          throw new Error(`Google auth error: ${error}`);
        }

        if (!authCode) {
          throw new Error("Authorization code not found");
        }

        const response = await api.post("/auth/google", null, {
          params: {
            code: authCode,
          },
        });
        localStorage.setItem(ACCESS_TOKEN, response.data.access_token);

        navigate("/");
      } catch (err) {
        navigate("/login", { state: { error: err.message } });
        throw new Error("Authentication failed:", err);
      }
    };

    handleGoogleCallback();
  }, [location, navigate]);

  return (
    <Container>
      <Row className="justify-content-center my-3">
        <Row className="my-5">
          <LogoCommon className="text-center" />
        </Row>
        <Col xs="auto" className="d-flex align-items-center gap-3">
          <h5 className="mb-0">The confirmation process</h5>
          <Spinner animation="border" />
        </Col>
      </Row>
    </Container>
  );
};

export default GoogleAuthCallback;
