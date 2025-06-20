import { Col, Container, Row } from "react-bootstrap";

// COMPONENTS
import { Logo } from "../components/Logo";
import UserForm from "../components/UserForm";

function Register() {
  return (
    <Container fluid>
      <Row className="align-items-center justify-content-center">
        <Col xs={12} sm={10} md={10} lg={8} xl={6} className="text-center">
          <div className="my-5">
            <Logo className="text-center" />
          </div>
          <UserForm method="register" />
        </Col>
      </Row>
    </Container>
  );
}
export default Register;
