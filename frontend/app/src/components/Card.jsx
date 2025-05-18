import { Card, Image, Row, Col } from "react-bootstrap";
import { ButtonFactory, ShowHideButton } from "./Buttons";
import imgUrl from "./static/default.jpg";

export function WordCard() {
  const status = "Новое слово";
  const content = {
    wrd: "banana",
    translation: "Банан",
    transcription: "[bəˈnɑːnə]",
  };

  return (
    <Card>
      <Card.Header className="d-flex justify-content-between align-items-center custom-light-bg">
        <div>{status}</div>
        {ButtonFactory.createReturnButton()}
      </Card.Header>
      <Card.Body>
        <h1 className="mb-3">{content.wrd}</h1>
        <Card.Subtitle className="mb-4">{content.transcription}</Card.Subtitle>
        <Row className="justify-content-center my-3">
          <Col xs={10} md={8} lg={6}>
            <div className="ratio ratio-4x3">
              <Image
                src={imgUrl}
                alt={content.wrd}
                rounded
                className="object-fit-cover"
              />
            </div>
          </Col>
        </Row>
      </Card.Body>
      <Card.Footer className="d-flex justify-content-between align-items-center custom-light-bg">
        {ButtonFactory.createCommonButton("Уже знаю")}
        <ShowHideButton />
        {ButtonFactory.createCommonButton("Не знаю")}
      </Card.Footer>
    </Card>
  );
}
