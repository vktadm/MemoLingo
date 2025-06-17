import {
  faCalendar,
  faCheck,
  faEnvelope,
  faUser,
  faUserEdit,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { format, parseISO } from "date-fns";
import { useEffect, useState } from "react";
import { Card, Spinner } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import api from "../Api";
import { ButtonFactory } from "../components/Buttons";

export function Profile() {
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    username: "",
    email: "",
    joinDate: "",
    is_active: false,
  });
  const [isLoading, setIsLoading] = useState(true);
  const [isSendingEmail, setIsSendingEmail] = useState(false);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await api.get("/users/about");
        setUserData({
          username: response.data.username,
          email: response.data.email,
          joinDate: format(parseISO(response.data.join_date), "d MMMM yyyy"),
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

  const handleEmailConfirmation = async () => {
    setIsSendingEmail(true);
    try {
      await api.post("/users/send_confirmation_email", {
        email: userData.email,
      });
      alert("A confirmation email has been sent to your email address.");
    } catch (error) {
      console.error(error);
    } finally {
      setIsSendingEmail(false);
    }
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
        <div className="d-flex align-items-center justify-content-center">
          <h4 className="me-2">{userData.username}</h4>
          {ButtonFactory.createIconButton("Edit", faUserEdit, {
            variant: "primary",
            size: "sm",
          })}
        </div>
      </div>

      {/* Карточка с email */}
      <Card className="mb-3 shadow-sm">
        <Card.Body className="py-3">
          <div className="d-flex align-items-center">
            <FontAwesomeIcon icon={faEnvelope} className="me-3 text-muted" />
            <div className="text-muted small mx-1">Email</div>
            <div className="d-flex align-items-center">
              <span className="mx-1">{userData.email}</span>
              {userData.is_active
                ? ButtonFactory.createIconButton("Сonfirmed", faCheck, {
                    variant: "success",
                    size: "sm",
                    disabled: true,
                  })
                : ButtonFactory.createIconButton("Сonfirm", faEnvelope, {
                    variant: "danger",
                    size: "sm",
                    onClick: () => handleEmailConfirmation(),
                    disabled: isSendingEmail,
                  })}
            </div>
          </div>
        </Card.Body>
      </Card>

      {/* Карточка с датой регистрации */}
      <Card className="mb-3 shadow-sm">
        <Card.Body className="py-3">
          <div className="d-flex align-items-center">
            <FontAwesomeIcon icon={faCalendar} className="me-3 text-muted" />
            <div className="text-muted small mx-1">Join date:</div>
            <div>{userData.joinDate}</div>
          </div>
        </Card.Body>
      </Card>
    </div>
  );
}

export default Profile;
