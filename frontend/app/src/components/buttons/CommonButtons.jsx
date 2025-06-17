import { Button } from "react-bootstrap";

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

class CommonButton extends ABSButton {
  constructor(text = "Ok", props = {}) {
    super(text, "light", props);
  }

  render() {
    return this.renderContent(this.text);
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

export const CommonButtonFactory = {
  createCommonButton: (text, props) => new CommonButton(text, props).render(),
  createSaveButton: (text, props) => new SaveButton(text, props).render(),
  createConfirmButton: (text, props) => new ConfirmButton(text, props).render(),
  createDeleteButton: (text, props) => new DeleteButton(text, props).render(),
};
