import { Container, Row } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import { ReturnButtonFactory } from "../components/buttons/ReturnButtons";

function NotFound() {
  const navigate = useNavigate();
  const handleClick = () => {
    navigate("/");
  };
  return (
    <Container className="m-5 text-center">
      <Row>
        <h1>404</h1>
        <h3>Page not found...</h3>
        <div>
          {ReturnButtonFactory.createCommonReturnButton(
            "Go back to the main page",
            {
              onClick: handleClick,
            }
          )}
        </div>
      </Row>
    </Container>
  );
}
export default NotFound;
