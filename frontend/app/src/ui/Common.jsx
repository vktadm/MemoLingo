import { Container, Row, Col, Navbar } from "react-bootstrap";

import { LogoCommon } from "../components/Logo";
import { Progress } from "../components/Progress";

export function Common() {
  return (
    <div className="m-3">
      <div className="m-3">
        <h3>LogoCommon</h3>
        <LogoCommon />
      </div>
      <div className="m-3">
        <h3>Progress</h3>
        <Progress now={5} total={10} />
      </div>
    </div>
  );
}
