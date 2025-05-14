import { useState } from "react";
import { Container, Navbar, ButtonGroup, Button, Badge } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUser, faSignOutAlt } from "@fortawesome/free-solid-svg-icons";

function MainNavbar() {
  const username = "example@gmail.com";
  return (
    <Navbar className="justify-content-between m-4">
      <Container>
        <Navbar.Brand href="#home">MemoLingo</Navbar.Brand>
        <ButtonGroup>
          <Button variant="primary">Изучать</Button>
          <Button variant="light text-primary">Словарь</Button>
          <Button variant="light text-primary">Настройки</Button>
        </ButtonGroup>
        <ButtonGroup>
          <Button variant="light">{username}</Button>
          <Button variant="light">
            <FontAwesomeIcon icon={faSignOutAlt} size="lg" />
          </Button>
          <Button variant="light">
            <FontAwesomeIcon icon={faUser} size="lg" />
            <Badge pill bg="danger">
              99+
            </Badge>
          </Button>
        </ButtonGroup>
      </Container>
    </Navbar>
  );
}

export default MainNavbar;
