import { BrowserRouter, Routes, Route } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/App.css";

import Home from "./pages/Home";
import UI from "./pages/UI";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/ui" element={<UI />} />
          <Route path="*" element={<NotFound />}></Route>
          {/* <Route path="/login" element={<Login />} /> */}
          {/* <Route path="/logout" element={<Logout />} /> */}
          {/* <Route path="/register" element={<RegisterAndLogout />} /> */}
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
