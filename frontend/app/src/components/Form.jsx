import { useState } from "react";
import { Form, Card } from "react-bootstrap";
import { ButtonFactory } from "./Buttons";

function UserForm() {
  return (
    <Card className="mx-auto" style={{ maxWidth: "400px" }}>
      <Card.Body>
        <Form className="text-center">
          <h3 className="my-4">Авторизация</h3>
          <Form.Group className="my-3" controlId="">
            <Form.Control type="text" placeholder="Имя пользователя" />
          </Form.Group>
          <Form.Group className="my-3" controlId="">
            <Form.Control type="password" placeholder="Пароль" />
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
