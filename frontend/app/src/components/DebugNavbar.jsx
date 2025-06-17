import { Container, Nav, Navbar } from "react-bootstrap";

function DebugNav({ activeKey = "home" }) {
  return (
    <Navbar>
      <Container fluid className="justify-content-start">
        <Navbar.Brand>Debug Navbar</Navbar.Brand>
        <Nav variant="tabs" activeKey={activeKey}>
          <Nav.Item>
            <Nav.Link eventKey="home" href="/">
              Home
            </Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="profile" href="/profile">
              Profile
            </Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="register" href="/register">
              Register
            </Nav.Link>
          </Nav.Item>
          <Nav.Link eventKey="login" href="/login">
            Login
          </Nav.Link>
          <Nav.Item>
            <Nav.Link eventKey="logout" href="/logout">
              Logout
            </Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="ui" href="/ui">
              UI components
            </Nav.Link>
          </Nav.Item>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default DebugNav;
