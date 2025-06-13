import { useState } from "react";
import { Container, Row } from "react-bootstrap";

import { UserNav } from "../components/UserNav";

export function User() {
  const [user, setUser] = useState(null);

  const handleLogin = () => setUser({ name: "username" });
  const handleLogout = () => setUser(null);
  const handleProfile = () => navigate("/profile");

  return (
    <div className="m-3">
      <h3>UserNav</h3>
      <UserNav
        username={user?.name}
        onLogin={handleLogin}
        onLogout={handleLogout}
        onProfile={handleProfile}
      />
    </div>
  );
}
