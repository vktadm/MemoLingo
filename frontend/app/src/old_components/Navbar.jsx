import { Container, Navbar } from "react-bootstrap";

import { GroupButton } from "./Buttons";
import { LogoCommon } from "./Logo";
import { UserNav } from "./UserNav";

function MainNavbar({ navButtons, userData, handleButtonClick }) {
  return (
    <Navbar className="justify-content-between m-4">
      <Container>
        <Navbar.Brand href="#home">
          <LogoCommon />
        </Navbar.Brand>
        {new GroupButton(navButtons, handleButtonClick).render()}
        <UserNav username={userData.username} />
      </Container>
    </Navbar>
  );
}

export default MainNavbar;
