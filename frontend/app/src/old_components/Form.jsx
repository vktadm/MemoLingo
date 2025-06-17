import { useState } from "react";
import { Card, Form, Spinner } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import api from "../Api";
import { ACCESS_TOKEN } from "../api/constants";
import { ButtonFactory } from "./Buttons";

function UserForm({ route, method }) {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const isLogin = method === "login";
  const formTitle = isLogin ? "Login" : "Register";

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    const data = isLogin
      ? { username, password }
      : { username, password, email };

    try {
      const response = await api.post(route, data);
      if (isLogin) {
        localStorage.setItem(ACCESS_TOKEN, response.data.access_token);
        const targetPath = response.data.user_role === "admin" ? "/ui" : "/";
        navigate(targetPath, { replace: true });
      } else {
        alert("Registration successful! Please login.");
        navigate("/login", { replace: true });
      }
    } catch (error) {
      if (error.response) {
        const { status, data } = error.response;
        alert(data.detail);
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleGoogleLogin = async () => {
    window.open("http://localhost:8000/api/v1/auth/login/google", "_blank");
  };

  return (
    <Card className="mx-auto" style={{ maxWidth: "400px" }}>
      <Card.Body>
        <Form className="text-center" onSubmit={handleSubmit}>
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
          {!isLogin && (
            <Form.Group className="my-3" controlId="email">
              <Form.Control
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                disabled={isLoading}
                required
              />
            </Form.Group>
          )}
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
            {ButtonFactory.createGoogleButton(undefined, {
              className: "flex-grow-1",
              onClick: handleGoogleLogin,
              disabled: isLoading,
            })}
            {ButtonFactory.createConfirmButton(
              isLoading ? (
                <>
                  <Spinner
                    as="span"
                    animation="border"
                    size="sm"
                    role="status"
                    aria-hidden="true"
                    className="me-2"
                  />
                  Processing...
                </>
              ) : (
                "Confirm"
              ),
              {
                type: "submit",
                className: "flex-grow-1",
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
