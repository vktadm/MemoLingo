import { BrowserRouter, Routes, Route } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/App.css";

import Home from "./pages/Home";
import UI from "./pages/UI";
import NotFound from "./pages/NotFound";
import Registeration from "./pages/Registration";
import Login from "./pages/Login";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ui" element={<UI />} />
          <Route path="/login" element={<Login />} />
          {/* <Route path="/logout" element={<Logout />} /> */}
          <Route path="/register" element={<Registeration />} />
          <Route path="*" element={<NotFound />}></Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
