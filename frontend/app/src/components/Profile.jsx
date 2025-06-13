import {
  faCalendar,
  faCheck,
  faEnvelope,
  faUser,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useEffect, useState } from "react";
import { Badge, Card, Spinner } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import api from "../Api";

export function Profile() {
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    username: "",
    email: "",
    joinDate: "",
    is_active: false,
  });
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await api.get("/users/about");
        setUserData({
          username: response.data.username,
          email: response.data.email,
          name: response.data.name,
          joinDate: "2025-01-01",
          is_active: response.data.is_active,
        });
      } catch (error) {
        console.error(error);
        navigate("/login");
      } finally {
        setIsLoading(false);
      }
    };

    fetchUserData();
  }, [navigate]);

  const handleProfileEdit = () => {
    // navigate("/profile/edit");
  };

  if (isLoading) {
    return <Spinner animation="border" variant="primary" />;
  }

  return (
    <div className="container py-4">
      {/* Заголовок профиля */}
      <div className="text-center mb-4">
        <FontAwesomeIcon
          icon={faUser}
          className="mb-3"
          size="2x"
          style={{ color: "#6c757d" }}
        />
        <h4 className="mb-0">{userData.username}</h4>
      </div>

      {/* Карточка с email */}
      <Card className="mb-3 shadow-sm">
        <Card.Body className="py-3">
          <div className="d-flex align-items-center">
            <FontAwesomeIcon icon={faEnvelope} className="me-3 text-muted" />
            <div className="text-muted small mx-1">Email</div>
            <div className="d-flex align-items-center">
              <span className="mx-1">{userData.email}</span>
              {userData.is_active ? (
                <Badge bg="success" className="px-1">
                  <FontAwesomeIcon icon={faCheck} />
                </Badge>
              ) : (
                <Badge bg="danger" className="py-1">
                  Не подтвержден
                </Badge>
              )}
            </div>
          </div>
        </Card.Body>
      </Card>

      {/* Карточка с датой регистрации */}
      <Card className="mb-3 shadow-sm">
        <Card.Body className="py-3">
          <div className="d-flex align-items-center">
            <FontAwesomeIcon icon={faCalendar} className="me-3 text-muted" />
            <div className="text-muted small mx-1">Дата регистрации</div>
            <div>{userData.joinDate}</div>
          </div>
        </Card.Body>
      </Card>
    </div>
  );
}

export default Profile;
