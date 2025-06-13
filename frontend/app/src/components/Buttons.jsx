import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faCheck,
  faUndo,
  faEyeSlash,
  faEye,
  faEnvelope,
} from "@fortawesome/free-solid-svg-icons";
import { faGoogle } from "@fortawesome/free-brands-svg-icons";
import { Button, ToggleButton, ButtonGroup } from "react-bootstrap";

// Абстрактный базовый класс для кнопок
class ABSButton {
  constructor(
    text = "Кнопка",
    variant = "light",
    onClick = () => {},
    props = {}
  ) {
    this.text = text;
    this.variant = variant;
    this.onClick = onClick;
    this.props = props;
  }

  renderContent(content) {
    return (
      <Button
        variant={this.variant}
        className={this.variant === "light" ? "btn-custom-light" : ""}
        onClick={this.onClick}
        {...this.props}
      >
        {content}
      </Button>
    );
  }
}

export class SaveButton extends ABSButton {
  constructor(text = "Сохранить", onClick = () => {}, props = {}) {
    super(text, "success", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class CommonButton extends ABSButton {
  constructor(text = "Ок", onClick = () => {}, props = {}) {
    super(text, "light", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class ConfirmButton extends ABSButton {
  constructor(text = "Ок", onClick = () => {}, props = {}) {
    super(text, "primary", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class DeleteButton extends ABSButton {
  constructor(text = "Удалить", onClick = () => {}, props = {}) {
    super(text, "danger", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}
class ReturnButton extends ABSButton {
  constructor(text = "Вернуть", onClick = () => {}, props = {}) {
    super(text, "link", onClick, props);
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="text-decoration-none"
        onClick={this.onClick}
        {...this.props}
      >
        <span className="me-2">{this.text}</span>
        <FontAwesomeIcon icon={faUndo} size="lg" />
      </Button>
    );
  }
}

class LinkButton extends ABSButton {
  constructor(text = "Ок", onClick = () => {}, fa = faCheck, props = {}) {
    super(text, "link", onClick, props);
    this.fa = fa;
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="text-decoration-none text-dark"
        onClick={this.onClick}
        {...this.props}
      >
        <FontAwesomeIcon icon={this.fa} size="lg" className="me-2" />
        <span>{this.text}</span>
      </Button>
    );
  }
}

class GoogleButton extends ABSButton {
  constructor(text = "Google", onClick = () => {}, props = {}) {
    super(text, "light", onClick, props);
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="d-flex align-items-center justify-content-center gap-2 btn-custom-light"
        disabled={this.isDisabled}
      >
        <FontAwesomeIcon icon={faEnvelope} size="lg" />
        <span>{this.text}</span>
      </Button>
    );
  }
}

export function ToggleButtonCheck({ id }) {
  const [checked, setChecked] = useState(false);

  return (
    <ToggleButton
      id={id}
      type="checkbox"
      variant="outline-primary"
      checked={checked}
      value="1"
      onChange={(e) => setChecked(e.currentTarget.checked)}
      size="sm"
    >
      <FontAwesomeIcon icon={faCheck} />
    </ToggleButton>
  );
}

export class GroupButton {
  constructor(buttons, onButtonClick) {
    this.buttons = buttons;
    this.onButtonClick = onButtonClick;
  }

  render() {
    return (
      <ButtonGroup>
        {this.buttons.map((item) => (
          <Button
            key={item.id}
            variant={item.selected ? "primary" : "light"}
            onClick={() => this.onButtonClick(item.id)} // Передаем id при клике
          >
            {item.title}
          </Button>
        ))}
      </ButtonGroup>
    );
  }
}

export function ShowHideButton({ onToggle, isVisible }) {
  return (
    <Button
      variant="light"
      className="btn-custom-light"
      onClick={onToggle}
      aria-label={isVisible ? "Скрыть" : "Показать"}
    >
      <FontAwesomeIcon icon={isVisible ? faEyeSlash : faEye} className="mx-5" />
    </Button>
  );
}

// Фабрика для удобного использования
export const ButtonFactory = {
  createSaveButton: (text, onClick, props) =>
    new SaveButton(text, onClick, props).render(),
  createCommonButton: (text, onClick, props) =>
    new CommonButton(text, onClick, props).render(),
  createConfirmButton: (text, onClick, props) =>
    new ConfirmButton(text, onClick, props).render(),
  createDeleteButton: (text, onClick, props) =>
    new DeleteButton(text, onClick, props).render(),
  createReturnButton: (text, onClick, props) =>
    new ReturnButton(text, onClick, props).render(),
  createGoogleButton: (text, onClick, props) =>
    new GoogleButton(text, onClick, props).render(),
  createLinkButton: (text, onClick, fa, props) =>
    new LinkButton(text, onClick, fa, props).render(),
};
