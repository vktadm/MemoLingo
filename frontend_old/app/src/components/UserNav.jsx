import { useState } from "react";
import { ButtonGroup, Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faSignOutAlt,
  faUser,
  faSignInAlt,
} from "@fortawesome/free-solid-svg-icons";

export function UserNav({ username, ...props }) {
  return username ? (
    <AuthUserView username={username} {...props} />
  ) : (
    <GuestUserView {...props} />
  );
}
function AuthUserView({ username, onLogout, onProfile }) {
  // ... рендеринг для авторизованного пользователя
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
        onClick={onLogout}
        title="Выйти"
      >
        <FontAwesomeIcon icon={faSignOutAlt} size="lg" />
      </Button>
    </ButtonGroup>
  );
}

function GuestUserView({ onLogin }) {
  // ... рендеринг для гостя
  return (
    <Button variant="light" className="mx-5" onClick={onLogin}>
      <FontAwesomeIcon icon={faSignInAlt} className="me-2" />
      Войти
    </Button>
  );
}
