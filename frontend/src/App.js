import React, { useContext } from "react";

import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import AuthNav from "./components/AuthNav";
import Nav from "./components/Nav";
import AuthContext from "./context/AuthContext";
import Activation from "./pages/Activation";
import ConfirmNewPassword from "./pages/ConfirmNewPassword";
import AddChannel from "./pages/dashboard/AddChannel";
import Dashboard from "./pages/dashboard/Dashboard";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Payment from "./pages/Payment";
import PaymentCancel from "./pages/PaymentCancel";
import PaymentSuccess from "./pages/PaymentSuccess";
import Register from "./pages/Register";
import ResetPassword from "./pages/ResetPassword";
import { ToastContainer } from 'react-toastify'
import PageNotFound from "./pages/PageNotFound";

function App() {

  const { isAuthenticated } = useContext(AuthContext)



  const ProtectedRoute = ({ user, children }) => {
    if (!user) {
      return <Navigate to="/login" replace />;

    }

    return children;
  };

  return (

    <Router>
      <div className="w-full h-screen" >
       { localStorage.getItem('isAuthenticated') ? <AuthNav/> : <Nav/> }
        <Routes>

          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route
            path="/dashboard"
            element={
              <ProtectedRoute user={isAuthenticated ? true : localStorage.getItem('isAuthenticated')}>
                <Dashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/dashboard/add-channel"
            element={
              <ProtectedRoute user={isAuthenticated ? true : localStorage.getItem('isAuthenticated')}>
                <AddChannel />
              </ProtectedRoute>
            }
          />

          <Route path="/reset-password" element={<ResetPassword />} />
          <Route path="*" element={<PageNotFound />} />
          <Route path="/activate/:uid/:token" element={<Activation />} />
          <Route path="/password/reset/confirm/:uid/:token" element={<ConfirmNewPassword />} />

          <Route
            path="/subscription"
            element={
              <ProtectedRoute user={isAuthenticated ? true : localStorage.getItem('isAuthenticated')}>
                <Payment />
              </ProtectedRoute>
            }
          />

          <Route
            path="/subscription/success/:CHECKOUT_SESSION_ID"
            element={
              <ProtectedRoute user={isAuthenticated ? true : localStorage.getItem('isAuthenticated')}>
                <PaymentSuccess />
              </ProtectedRoute>
            }
          />

          <Route
            path="/subscription/failed/"
            element={
              <ProtectedRoute user={isAuthenticated ? true : localStorage.getItem('isAuthenticated')}>
                <PaymentCancel />
              </ProtectedRoute>
            }
          />

        </Routes>
        <ToastContainer/>
      </div>
    </Router>

  );
}

export default App;
