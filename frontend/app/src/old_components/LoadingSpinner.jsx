import { Col, Row, Spinner } from "react-bootstrap";

import { LogoCommon } from "./Logo";

export function LoadingSpinner() {
  return (
    <Row className="justify-content-center my-5">
      <Col xs="auto" className="d-flex align-items-center gap-3">
        <LogoCommon className="text-center" />
        <Spinner animation="border" role="status"></Spinner>
      </Col>
    </Row>
  );
}
