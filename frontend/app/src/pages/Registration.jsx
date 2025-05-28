import { useState } from "react";
import { Container, Row, Col, Card } from "react-bootstrap";

function Registration() {
  const userData = { id: 1, username: "user", email: "example.com" };
  return (
    <Container fluid>
      <Row className="justify-content-center">
        <Col>Регистрация</Col>
      </Row>
    </Container>
  );
}

export default Registration;
