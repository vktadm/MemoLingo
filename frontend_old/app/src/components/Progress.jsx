import { useState } from "react";
import ProgressBar from "react-bootstrap/ProgressBar";

export function Progress({ now, total }) {
  const percent = parseInt((now / total) * 100, 10);
  return <ProgressBar now={percent} label={`${now} / ${total}`} />;
}
