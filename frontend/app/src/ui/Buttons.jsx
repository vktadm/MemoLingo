import { Container, Row } from "react-bootstrap";
import { useState } from "react";

import {
  ButtonFactory,
  ShowHideButton,
  GroupButton,
  ToggleButtonCheck,
} from "../components/Buttons";

export function Buttons() {
  const [activeContent, setActiveContent] = useState("btn1");

  const handleButtonClick = (contentId) => {
    setActiveContent(contentId);
  };

  const buttons = [
    {
      id: "btn1",
      title: "btn1",
      selected: activeContent === "btn1",
    },
    {
      id: "btn2",
      title: "btn2",
      selected: activeContent === "btn2",
    },
    {
      id: "btn3",
      title: "btn3",
      selected: activeContent === "btn3",
    },
  ];

  const buttonComponents = [
    {
      title: "SaveButton",
      component: ButtonFactory.createSaveButton(),
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "CommonButton",
      component: ButtonFactory.createCommonButton(),
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "ConfirmButton",
      component: ButtonFactory.createConfirmButton(),
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "DeleteButton",
      component: ButtonFactory.createDeleteButton(),
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "GoogleButton",
      component: ButtonFactory.createGoogleButton(),
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "ReturnWordButton",
      component: ButtonFactory.createReturnButton(),
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "ToggleButtonCheck",
      component: (id) => <ToggleButtonCheck id={id} />,
      layouts: ["d-grid gap-2", ""],
      needsId: true,
    },
    {
      title: "ShowHideButton - hide",
      component: <ShowHideButton isVisible={true} />,
      layouts: ["d-grid gap-2", ""],
    },
    {
      title: "GroupButton",
      component: new GroupButton(buttons, handleButtonClick).render(),
      layouts: ["d-grid gap-2", ""],
    },
  ];

  return (
    <Container>
      {buttonComponents.map((item, index) => (
        <Row key={index} className="mt-3">
          <h3>{item.title}</h3>
          {item.layouts.map((layout, layoutIndex) => (
            <div key={layoutIndex} className={`my-3 ${layout}`}>
              {item.needsId ? item.component(layoutIndex + 1) : item.component}
            </div>
          ))}
        </Row>
      ))}
    </Container>
  );
}
