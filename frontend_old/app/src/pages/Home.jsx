import { useState } from "react";
import { faBook, faPlus, faClock } from "@fortawesome/free-solid-svg-icons";
import { Container, Row, Col, Card } from "react-bootstrap";

import MainNavbar from "../components/Navbar";
import { ButtonFactory } from "../components/Buttons";

function Home() {
  const userData = { id: 1, username: "user", email: "example.com" };
  const usereStatistics = { dayLearnTotal: 10, dayLearn: 3, revise: 136 };

  const [activeContent, setActiveContent] = useState("learn");
  const navButtons = [
    {
      id: "learn",
      title: "Учить",
      selected: activeContent === "learn",
    },
    {
      id: "dictionary",
      title: "Словарь",
      selected: activeContent === "dictionary",
    },
    {
      id: "settings",
      title: "Настройки",
      selected: activeContent === "settings",
    },
  ];

  const handleButtonClick = (contentId) => {
    setActiveContent(contentId);
  };
  return (
    <Container fluid>
      <MainNavbar
        navButtons={navButtons}
        userData={userData}
        handleButtonClick={handleButtonClick}
      />
      <Row className="justify-content-center">
        <Col>
          {activeContent === navButtons[0].id && (
            <>
              <Card className="my-3">
                <Card.Body className="d-flex justify-content-between align-items-center">
                  {ButtonFactory.createLinkButton(
                    "Категории на изучении",
                    undefined,
                    faBook
                  )}
                </Card.Body>
              </Card>

              <Card className="my-3">
                <Card.Body className="d-flex justify-content-between align-items-center">
                  {ButtonFactory.createLinkButton(
                    "Изучать новые слова",
                    undefined,
                    faPlus
                  )}
                  <div>
                    Заученно сегодня:{" "}
                    <strong>
                      {usereStatistics.dayLearn} /{" "}
                      {usereStatistics.dayLearnTotal}
                    </strong>
                  </div>
                </Card.Body>
              </Card>

              <Card className="my-3">
                <Card.Body className="d-flex justify-content-between align-items-center">
                  {ButtonFactory.createLinkButton(
                    "Повторить слова",
                    undefined,
                    faClock
                  )}
                  <div>
                    На повторении: <strong>{usereStatistics.revise}</strong>
                  </div>
                </Card.Body>
              </Card>
            </>
          )}

          {activeContent === navButtons[1].id && (
            <Card>
              <Card.Body className="d-flex justify-content-between align-items-center">
                Словарь
              </Card.Body>
            </Card>
          )}

          {activeContent === navButtons[2].id && (
            <Card>
              <Card.Body className="d-flex justify-content-between align-items-center">
                Настройки
              </Card.Body>
            </Card>
          )}
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
