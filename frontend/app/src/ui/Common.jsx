import { Container, Row, Col, Navbar } from "react-bootstrap";

import { LogoCommon } from "../components/Logo";
import { Progress } from "../components/Progress";
import { WordCard } from "../components/Card";

export function Common() {
  return (
    <div className="m-3">
      <div className="mt-3">
        <h3>LogoCommon</h3>
        <LogoCommon />
      </div>

      <div className="mt-3">
        <h3>Progress</h3>
        <Progress now={5} total={10} />
      </div>

      <div className="mt-3">
        <h3>WordCard - Learn</h3>
        <div className="background-main">
          <Row className="justify-content-center">
            <Col xs={10} md={8} lg={6}>
              <div className="m-3">
                <WordCard />
              </div>
            </Col>
          </Row>
        </div>
      </div>
    </div>
  );
}
