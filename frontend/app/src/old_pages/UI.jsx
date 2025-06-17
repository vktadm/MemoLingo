import { useState } from "react";
import { Container, Row, Col, Navbar } from "react-bootstrap";

import { GroupButton } from "../components/Buttons";
import { Common } from "../ui/Common";
import { Buttons } from "../ui/Buttons";
import { User } from "../ui/User";

function UI() {
  const [activeContent, setActiveContent] = useState("common");

  // Данные для кнопок
  const buttons = [
    {
      id: "common",
      title: "Основные",
      selected: activeContent === "common",
    },
    {
      id: "buttons",
      title: "Кнопки",
      selected: activeContent === "buttons",
    },
    {
      id: "user",
      title: "Пользователь",
      selected: activeContent === "user",
    },
  ];

  const handleButtonClick = (contentId) => {
    setActiveContent(contentId);
  };
  return (
    <Container>
      <Navbar className="justify-content-center m-4">
        {new GroupButton(buttons, handleButtonClick).render()}
      </Navbar>
      <Row className="justify-content-center custom-light-bg m-4">
        {activeContent === "common" && <Common />}
        {activeContent === "buttons" && <Buttons />}
        {activeContent === "user" && <User />}
      </Row>
    </Container>
  );
}

export default UI;
