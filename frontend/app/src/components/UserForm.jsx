import { useState } from "react";
import { Card, Form, Spinner } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

// COMPONENTS
import { useAuth } from "../hooks/AuthContext";
import { CommonButtonFactory } from "./buttons/CommonButtons";
import { IconButtonFactory } from "./buttons/IconButtons";

function UserForm({ route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const { login, isLoading } = useAuth();
  const navigate = useNavigate();

  const isLogin = method === "login";
  const formTitle = isLogin ? "Login" : "Register";

  const handleLogin = async (e) => {
    e.preventDefault();
    const credentials = isLogin
      ? { username, password }
      : { username, password, email };

    if (isLogin) {
      const user = await login(credentials);
      if (user) {
        navigate(user.role === "admin" ? "/ui" : "/profile", { replace: true });
      }
    } else {
      alert("Register");
    }
  };
  const handleGoogleLogin = async (e) => {
    e.preventDefault();
  };

  return (
    <Card className="mx-auto" style={{ maxWidth: "400px" }}>
      <Card.Body>
        <Form className="text-center" onSubmit={handleLogin}>
          <h3 className="my-4">{formTitle}</h3>
          <Form.Group className="my-3" controlId="">
            <Form.Control
              type="text"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              disabled={isLoading}
            />
          </Form.Group>
          <Form.Group className="my-3" controlId="">
            <Form.Control
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              disabled={isLoading}
            />
          </Form.Group>
          <div className="d-flex justify-content-center gap-3 my-3">
            {IconButtonFactory.createGoogleButton({
              className: "flex-grow-1",
              onClick: handleGoogleLogin,
              disabled: isLoading,
            })}
            {CommonButtonFactory.createConfirmButton(
              isLoading ? (
                <>
                  <Spinner
                    as="span"
                    animation="border"
                    size="sm"
                    className="me-2"
                  ></Spinner>
                  Processing...
                </>
              ) : (
                "Confirm"
              ),
              {
                type: "submit",
                className: "flex-grow-1",
                onClick: handleLogin,
                disabled: isLoading,
              }
            )}
          </div>
        </Form>
      </Card.Body>
    </Card>
  );
}

export default UserForm;
