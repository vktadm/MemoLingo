import { faUndo } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Button } from "react-bootstrap";

// Абстрактный базовый класс для кнопок
class ABSReturnButton {
  constructor(text = "", variant = "light", props = {}) {
    this.text = text;
    this.variant = variant;
    this.props = props;
  }
  renderContent(content) {
    return (
      <Button
        variant={this.variant}
        className="text-decoration-none"
        {...this.props}
      >
        <span className="me-2">{content}</span>
        <FontAwesomeIcon icon={faUndo} size="lg" />
      </Button>
    );
  }
}

class CommonReturnButton extends ABSReturnButton {
  constructor(text = "Return", props = {}) {
    super(text, "link", props);
  }

  render() {
    return this.renderContent(this.text);
  }
}

export const ReturnButtonFactory = {
  createCommonReturnButton: (text, props) =>
    new CommonReturnButton(text, props).render(),
};
