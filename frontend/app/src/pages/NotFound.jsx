import { Container, Row, Col, Button } from "react-bootstrap";

import { ButtonFactory } from "../components/Buttons";

function NotFound() {
  const handleClick = () => {
    alert("Сохранение данных");
  };
  return (
    <Container className="m-5 text-center">
      <Row>
        <h1>404</h1>
        <h3>Страница не найдена</h3>
        <div>
          {ButtonFactory.createReturnButton(
            "Вернуться на главную",
            false,
            handleClick
          )}
        </div>
      </Row>
    </Container>
  );
}
export default NotFound;
