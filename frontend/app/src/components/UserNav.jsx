import { faSignOutAlt, faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Button, ButtonGroup } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import api from "../Api";
import { ACCESS_TOKEN } from "../constants";

export function UserNav({ username, onLogout, onProfile }) {
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await api.post("/auth/logout");
      localStorage.removeItem(ACCESS_TOKEN);
      navigate("/login");
      window.location.reload();
    } catch (error) {
      // Если API недоступно, просто выполняем локальный выход
      localStorage.removeItem(ACCESS_TOKEN);
      navigate("/login");
    }
  };
  return (
    <ButtonGroup>
      <Button variant="light" className="light" disabled>
        {username}
      </Button>
      <Button variant="light" className="light-white" onClick={onProfile}>
        <FontAwesomeIcon icon={faUser} size="lg" />
      </Button>
      <Button
        variant="light"
        className="btn-light"
        onClick={handleLogout}
        title="Выйти"
      >
        <FontAwesomeIcon icon={faSignOutAlt} size="lg" />
      </Button>
    </ButtonGroup>
  );
}
