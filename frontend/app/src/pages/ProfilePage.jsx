import { Container } from "react-bootstrap";
import { useAuth } from "../hooks/AuthContext";

function Profile() {
  const { isLogin, user } = useAuth();
  return (
    <Container>
      <h1>Profile</h1>
      <div>{user.username}</div>
    </Container>
  );
}
export default Profile;
