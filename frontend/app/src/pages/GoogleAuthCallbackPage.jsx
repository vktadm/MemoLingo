import { useEffect } from "react";
import { Col, Container, Row, Spinner } from "react-bootstrap";

import { Logo } from "../components/Logo";

const GoogleAuthCallback = () => {
  useEffect(() => {
    const handleGoogleCallback = async () => {};

    handleGoogleCallback();
  }, []);
  return (
    <Container>
      <Row className="justify-content-center my-3">
        <Row className="my-5">
          <Logo className="text-center" />
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
