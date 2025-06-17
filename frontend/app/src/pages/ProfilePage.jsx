import { Container } from "react-bootstrap";
import { useAuth } from "../hooks/AuthContext";

function Profile() {
  const { isLogin, user } = useAuth();
  return (
    <Container>
      <h1>Profile</h1>
      <div>
        ID: {user.id}
        <div>usernsme: {user.username}</div>
      </div>
    </Container>
  );
}
export default Profile;
