import { useState } from "react";
import { Card, Form } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

import api from "../Api";
import { ACCESS_TOKEN } from "../constants";
import { ButtonFactory } from "./Buttons";

function UserForm({ route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  // const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const name = method === "login" ? "Login" : "Register";

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await api.post(route, { username, password });
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access_token);
        navigate("/");
      } else {
        navigate("/login");
      }
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="mx-auto" style={{ maxWidth: "400px" }}>
      <Card.Body>
        <Form className="text-center" onSubmit={handleSubmit}>
          <h3 className="my-4">Авторизация</h3>
          <Form.Group className="my-3" controlId="">
            <Form.Control
              type="text"
              placeholder="Имя пользователя"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </Form.Group>
          <Form.Group className="my-3" controlId="">
            <Form.Control
              type="password"
              placeholder="Пароль"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </Form.Group>
          <div className="d-flex justify-content-center gap-3 my-3">
            {ButtonFactory.createGoogleButton(undefined, undefined, {
              className: "flex-grow-1",
            })}
            {ButtonFactory.createConfirmButton("Подтвердить", undefined, {
              type: "submit",
              className: "flex-grow-1",
            })}
          </div>
        </Form>
      </Card.Body>
    </Card>
  );
}

export default UserForm;
