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
    isDisabled = false,
    variant = "light",
    onClick = () => {},
    props = {}
  ) {
    this.text = text;
    this.isDisabled = isDisabled;
    this.variant = variant;
    this.onClick = onClick;
    this.props = props;
  }

  renderContent(content) {
    return (
      <Button
        variant={this.variant}
        disabled={this.isDisabled}
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
  constructor(
    text = "Сохранить",
    isDisabled = false,
    onClick = () => {},
    props = {}
  ) {
    super(text, isDisabled, "success", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class CommonButton extends ABSButton {
  constructor(text = "Ок", isDisabled = false, onClick = () => {}, props = {}) {
    super(text, isDisabled, "light", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class ConfirmButton extends ABSButton {
  constructor(text = "Ок", isDisabled = false, onClick = () => {}, props = {}) {
    super(text, isDisabled, "primary", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class DeleteButton extends ABSButton {
  constructor(
    text = "Удалить",
    isDisabled = false,
    onClick = () => {},
    props = {}
  ) {
    super(text, isDisabled, "danger", onClick, props);
  }

  render() {
    return this.renderContent(this.text);
  }
}
class ReturnButton extends ABSButton {
  constructor(
    text = "Вернуть",
    isDisabled = false,
    onClick = () => {},
    props = {}
  ) {
    super(text, isDisabled, "link", onClick, props);
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="text-decoration-none"
        disabled={this.isDisabled}
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
  constructor(
    text = "Ок",
    isDisabled = false,
    onClick = () => {},
    fa = faCheck,
    props = {}
  ) {
    super(text, isDisabled, "link", onClick, props);
    this.fa = fa;
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="text-decoration-none text-dark"
        disabled={this.isDisabled}
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
  constructor(
    text = "Google",
    isDisabled = false,
    onClick = () => {},
    props = {}
  ) {
    super(text, isDisabled, "light", onClick, props);
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

export function ToggleButtonCheck({ id, isDisabled = false }) {
  const [checked, setChecked] = useState(false);

  return (
    <ToggleButton
      id={id}
      type="checkbox"
      variant="outline-primary"
      checked={checked}
      disabled={isDisabled}
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
            disabled={item.isDisabled}
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
  createSaveButton: (text, isDisabled, onClick, props) =>
    new SaveButton(text, isDisabled, onClick, props).render(),
  createCommonButton: (text, isDisabled, onClick, props) =>
    new CommonButton(text, isDisabled, onClick, props).render(),
  createConfirmButton: (text, isDisabled, onClick, props) =>
    new ConfirmButton(text, isDisabled, onClick, props).render(),
  createDeleteButton: (text, isDisabled, onClick, props) =>
    new DeleteButton(text, isDisabled, onClick, props).render(),
  createReturnButton: (text, isDisabled, onClick, props) =>
    new ReturnButton(text, isDisabled, onClick, props).render(),
  createGoogleButton: (text, isDisabled, onClick, props) =>
    new GoogleButton(text, isDisabled, onClick, props).render(),
  createLinkButton: (text, isDisabled, onClick, fa, props) =>
    new LinkButton(text, isDisabled, onClick, fa, props).render(),
};
