import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Button } from "react-bootstrap";

class ABSIconButton {
  constructor(text = "", variant = "light", props = {}) {
    this.text = text;
    this.variant = variant;
    this.props = props;
  }

  renderContent(content) {
    return (
      <Button
        variant={this.variant}
        className="d-flex align-items-center justify-content-center gap-2 btn-custom-light"
        {...this.props}
      >
        <FontAwesomeIcon icon={faEnvelope} size="lg" className="mx-1" />
        <span>{content}</span>
      </Button>
    );
  }
}

class GoogleButton extends ABSIconButton {
  constructor(props = {}) {
    super("Google", "light", props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

export const IconButtonFactory = {
  createGoogleButton: (text, props) => new GoogleButton(text, props).render(),
};
