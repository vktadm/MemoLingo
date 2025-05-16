import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faCheck,
  faBook,
  faPlus,
  faClock,
} from "@fortawesome/free-solid-svg-icons";
import {
  Container,
  Row,
  Col,
  Button,
  Card,
  Accordion,
  ListGroup,
  ToggleButton,
} from "react-bootstrap";

import MainNavbar from "../components/Navbar";

function Home() {
  const revise_count = 100;
  const lear_total = 10;
  const learn_day = 3;
  return (
    <>
      <MainNavbar />
      <Container>
        <Row className="justify-content-center">
          <Col xs={12} md={10}>
            <Card className="m-4">
              <Card.Body>
                <Accordion defaultActiveKey="0">
                  <Accordion.Item eventKey="0">
                    <Accordion.Header>Категории на изучении</Accordion.Header>
                    <Accordion.Body>
                      <ListGroup>
                        <ListGroup.Item>
                          <div className="d-flex justify-content-between align-items-center">
                            <div>
                              <div className="d-flex align-items-center">
                                <FontAwesomeIcon
                                  icon={faBook}
                                  size="lg"
                                  className="me-2"
                                />
                                <span>Название категории</span>
                              </div>
                            </div>
                            <div>
                              <ToggleButton size="sm">
                                <FontAwesomeIcon icon={faCheck} />
                              </ToggleButton>
                            </div>
                          </div>
                        </ListGroup.Item>
                        <ListGroup.Item>
                          <div className="d-flex justify-content-between align-items-center">
                            <div>
                              <div className="d-flex align-items-center">
                                <FontAwesomeIcon
                                  icon={faBook}
                                  size="lg"
                                  className="me-2"
                                />
                                <span>Название категории</span>
                              </div>
                            </div>
                            <div>
                              <ToggleButton size="sm">
                                <FontAwesomeIcon icon={faCheck} />
                              </ToggleButton>
                            </div>
                          </div>
                        </ListGroup.Item>
                      </ListGroup>
                      <Button variant="success" className="mt-4">
                        Сохранить
                      </Button>
                    </Accordion.Body>
                  </Accordion.Item>
                </Accordion>
              </Card.Body>
            </Card>
            <Card className="m-4">
              <Card.Body>
                <div className="d-flex justify-content-between align-items-center">
                  <div className="d-flex align-items-center">
                    <FontAwesomeIcon icon={faPlus} size="lg" className="me-2" />
                    <span>Изучать новые слова</span>
                  </div>
                  <div>
                    Заученно сегодня: {learn_day} / {lear_total}
                  </div>
                </div>
              </Card.Body>
            </Card>
            <Card className="m-4">
              <Card.Body>
                <div className="d-flex justify-content-between align-items-center">
                  <div className="d-flex align-items-center">
                    <FontAwesomeIcon
                      icon={faClock}
                      size="lg"
                      className="me-2"
                    />
                    <span>Повторить слова</span>
                  </div>
                  <div>На повторении: {revise_count}</div>
                </div>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default Home;
