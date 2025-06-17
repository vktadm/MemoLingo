import {
  faCheck,
  faEnvelope,
  faEye,
  faEyeSlash,
  faUndo,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useState } from "react";
import { Button, ButtonGroup, ToggleButton } from "react-bootstrap";

// Абстрактный базовый класс для кнопок
class ABSButton {
  constructor(text = "", variant = "light", props = {}) {
    this.text = text;
    this.variant = variant;
    this.props = props;
  }

  renderContent(content) {
    return (
      <Button
        variant={this.variant}
        className={this.variant === "light" ? "btn-custom-light" : ""}
        {...this.props}
      >
        {content}
      </Button>
    );
  }
}

export class SaveButton extends ABSButton {
  constructor(text = "Save", props = {}) {
    super(text, "success", props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class CommonButton extends ABSButton {
  constructor(text = "Ok", props = {}) {
    super(text, "light", props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class ConfirmButton extends ABSButton {
  constructor(text = "Confirm", props = {}) {
    super(text, "primary", props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

class DeleteButton extends ABSButton {
  constructor(text = "Delete", props = {}) {
    super(text, "danger", props);
  }

  render() {
    return this.renderContent(this.text);
  }
}
class ReturnButton extends ABSButton {
  constructor(text = "Return", props = {}) {
    super(text, "link", props);
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="text-decoration-none"
        {...this.props}
      >
        <span className="me-2">{this.text}</span>
        <FontAwesomeIcon icon={faUndo} size="lg" />
      </Button>
    );
  }
}

class LinkButton extends ABSButton {
  constructor(text = "Ок", fa = faCheck, props = {}) {
    super(text, "link", props);
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
  constructor(text = "Google", props = {}) {
    super(text, "light", props);
  }

  render() {
    return (
      <Button
        variant={this.variant}
        className="d-flex align-items-center justify-content-center gap-2 btn-custom-light"
        disabled={this.isDisabled}
        {...this.props}
      >
        <FontAwesomeIcon icon={faEnvelope} size="lg" className="mx-1" />
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

class IconButton {
  constructor(text = "", fa = null, props = {}) {
    this.text = text;
    this.fa = fa;
    this.props = props;
  }

  render() {
    return (
      <Button {...this.props} className="badge">
        <FontAwesomeIcon icon={this.fa} className="mx-1" />
        {this.text}
      </Button>
    );
  }
}

// Фабрика для удобного использования
export const ButtonFactory = {
  createSaveButton: (text, props) => new SaveButton(text, props).render(),
  createCommonButton: (text, props) => new CommonButton(text, props).render(),
  createConfirmButton: (text, props) => new ConfirmButton(text, props).render(),
  createDeleteButton: (text, props) => new DeleteButton(text, props).render(),
  createReturnButton: (text, props) => new ReturnButton(text, props).render(),
  createGoogleButton: (text, props) => new GoogleButton(text, props).render(),
  createLinkButton: (text, fa, props) =>
    new LinkButton(text, fa, props).render(),
  createIconButton: (text, fa, props) =>
    new IconButton(text, fa, props).render(),
};
