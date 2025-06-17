import { Navigate } from "react-router-dom";
import { useAuth } from "../hooks/AuthContext";

export function ProtectedRoute({ children, adminOnly = false }) {
  const { user } = useAuth();

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (adminOnly && user.role !== "admin") {
    return <Navigate to="/" replace />;
  }

  return children;
}

export function ProtectedLoginRoute({ children }) {
  const { isLogin } = useAuth();

  if (isLogin) {
    return <Navigate to="/profile" replace />;
  }

  return children;
}
