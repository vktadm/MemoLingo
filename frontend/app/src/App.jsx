import { Route, BrowserRouter as Router, Routes } from "react-router-dom";

// BOOTSTRAP
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/App.css";

// PROTECTED
import {
  ProtectedLoginRoute,
  ProtectedRoute,
} from "./components/ProtectedRoute";

// PAGES
import GoogleAuthCallback from "./pages/GoogleAuthCallbackPage";
import Home from "./pages/HomePage";
import Login from "./pages/LoginPage";
import Logout from "./pages/LogoutPage";
import NotFound from "./pages/NotFoundPage";
import Profile from "./pages/ProfilePage";
import Register from "./pages/RegisterPage";
import UI from "./pages/UIPage";

// COMPONENTS
import NavWrapper from "./components/NavWrapper";

function App() {
  return (
    <Router>
      <NavWrapper />
      <Routes>
        {/* PUBLIC  */}
        <Route path="/" element={<Home />} />
        <Route
          path="/login"
          element={
            <ProtectedLoginRoute>
              <Login />
            </ProtectedLoginRoute>
          }
        />
        <Route path="/" element={<Home />} />
        <Route
          path="/register"
          element={
            <ProtectedLoginRoute>
              <Register />
            </ProtectedLoginRoute>
          }
        />
        <Route path="/google" element={<GoogleAuthCallback />} />
        {/* PROTECTED  */}
        <Route
          path="/logout"
          element={
            <ProtectedRoute>
              <Logout />
            </ProtectedRoute>
          }
        />
        <Route
          path="/profile"
          element={
            <ProtectedRoute>
              <Profile />
            </ProtectedRoute>
          }
        />
        <Route
          path="/ui"
          element={
            <ProtectedRoute adminOnly>
              <UI />
            </ProtectedRoute>
          }
        />
        {/* NOT FOUND  */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
