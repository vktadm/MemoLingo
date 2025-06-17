import { Link, Route, BrowserRouter as Router, Routes } from "react-router-dom";

// PAGES
import { ProtectedRoute } from "./components/ProtectedRoute";
import Home from "./pages/HomePage";
import Login from "./pages/LoginPage";
import Logout from "./pages/LogoutPage";
import NotFound from "./pages/NotFoundPage";
import Profile from "./pages/ProfilePage";
import UI from "./pages/UIPage";

// BOOTSTRAP
import "bootstrap/dist/css/bootstrap.min.css";
import "./styles/App.css";

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/profile">Profile</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/logout">Logout</Link>
          </li>
          <li>
            <Link to="/ui">UI components</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        {/* PUBLIC  */}
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        {/* PROTECTED  */}
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
// import { useEffect, useState } from "react";
// import { Container } from "react-bootstrap";
// import {
//   BrowserRouter,
//   Navigate,
//   Outlet,
//   Route,
//   Routes,
// } from "react-router-dom";

// import "bootstrap/dist/css/bootstrap.min.css";
// import "./styles/App.css";

// import api from "./Api";

// import { LoadingSpinner } from "./components/LoadingSpinner";
// import Home from "./pages/Home";
// import Login from "./pages/Login";
// import NotFound from "./pages/NotFound";
// import Registration from "./pages/Registration";
// import UI from "./pages/UI";

// // Компонент для защиты приватных маршрутов
// function PrivateRoute({ isAuthenticated }) {
//   return isAuthenticated ? <Outlet /> : <Navigate to="/login" replace />;
// }

// // Компонент для проверки прав администратора
// function AdminRoute({ userRole }) {
//   return userRole === "admin" ? <Outlet /> : <Navigate to="/" replace />;
// }

// function App() {
//   const [auth, setAuth] = useState({
//     isAuthenticated: false,
//     isLoading: true,
//     userRole: null,
//   });

//   useEffect(() => {
//     const checkAuth = async () => {
//       try {
//         const response = await api.get("/auth/check");
//         const { user_role } = response.data;

//         setAuth({
//           isAuthenticated: true,
//           isLoading: false,
//           userRole: user_role,
//         });
//       } catch (error) {
//         setAuth({
//           isAuthenticated: false,
//           isLoading: false,
//           userRole: null,
//         });
//       }
//     };

//     checkAuth();
//   }, []);

//   if (auth.isLoading) {
//     return (
//       <Container>
//         <LoadingSpinner></LoadingSpinner>
//       </Container>
//     );
//   }

//   return (
//     <BrowserRouter>
//       <Routes>
//         {/* Публичные маршруты */}
//         <Route
//           path="/login"
//           element={
//             auth.isAuthenticated ? <Navigate to="/" replace /> : <Login />
//           }
//         />
//         <Route
//           path="/register"
//           element={
//             auth.isAuthenticated ? (
//               <Navigate to="/" replace />
//             ) : (
//               <Registration />
//             )
//           }
//         />

//         {/* Защищенные маршруты */}
//         <Route
//           element={<PrivateRoute isAuthenticated={auth.isAuthenticated} />}
//         >
//           <Route path="/" element={<Home />} />

//           {/* Админ-маршруты */}
//           <Route element={<AdminRoute userRole={auth.userRole} />}>
//             <Route path="/ui" element={<UI />} />
//           </Route>
//         </Route>

//         {/* 404 страница */}
//         <Route path="*" element={<NotFound />} />
//       </Routes>
//     </BrowserRouter>
//   );
// }

// export default App;
