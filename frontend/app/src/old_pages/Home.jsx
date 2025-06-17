import { faBook, faClock, faPlus } from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from "react";
import { Card, Col, Container, Row } from "react-bootstrap";

import api from "../Api";
import { ButtonFactory } from "../components/Buttons";
import { LoadingSpinner } from "../components/LoadingSpinner";
import MainNavbar from "../components/Navbar";
import Profile from "../components/Profile";

function Home() {
  const [userData, setUserData] = useState({ id: 0, username: "" });
  const [loading, setLoading] = useState(true);
  const [userStatistics, setUserStatistics] = useState({
    dayLearnTotal: 0,
    dayLearn: 0,
    revise: 0,
  });
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const userResponse = await api.get("/users/about");
        setUserData(userResponse.data);
      } catch (err) {
        console.log("API Error:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const [activeContent, setActiveContent] = useState("learn");
  const navButtons = [
    {
      id: "learn",
      title: "Learn",
      selected: activeContent === "learn",
    },
    {
      id: "dictionary",
      title: "Dictionary",
      selected: activeContent === "dictionary",
    },
    {
      id: "settings",
      title: "Settings",
      selected: activeContent === "settings",
    },
  ];

  const handleButtonClick = (contentId) => {
    setActiveContent(contentId);
  };

  if (loading) {
    return (
      <Container>
        <LoadingSpinner />
      </Container>
    );
  }

  return (
    <Container>
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
                      {userStatistics.dayLearn} / {userStatistics.dayLearnTotal}
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
                    На повторении: <strong>{userStatistics.revise}</strong>
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

          {activeContent === navButtons[2].id && <Profile />}
        </Col>
      </Row>
    </Container>
  );
}

export default Home;
