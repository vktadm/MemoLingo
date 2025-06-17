import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

// COMPONENTS
import DebugNav from "./DebugNavbar";

function NavWrapper() {
  const location = useLocation();
  const [activeKey, setActiveKey] = useState("");

  useEffect(() => {
    const path = location.pathname;
    if (path === "/") setActiveKey("home");
    else if (path === "/login") setActiveKey("login");
    else if (path === "/register") setActiveKey("register");
    else if (path === "/profile") setActiveKey("profile");
    else if (path === "/ui") setActiveKey("ui");
    else if (path === "/logout") setActiveKey("logout");
    else setActiveKey("");
  }, [location]);

  return <DebugNav activeKey={activeKey} />;
}

export default NavWrapper;
