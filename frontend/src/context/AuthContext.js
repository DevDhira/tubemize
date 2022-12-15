import { createContext, useState, useReducer } from "react";
import React from "react";
import modAxios from "../custom/CustomAxios";


// import axios from "axios";
import authReducer from "./AuthReducer";
import axios from "axios";

const AuthContext = createContext()

export const AuthProvider = ({ children }) => {

    const [loading, setLoading] = useState(false)
    // const [isAuthenticated, setIsAuthenticated] = useState(false)
    //  // eslint-disable-next-line
    // const [authToken, setAuthToken] = useState('')


    const initialState = {
        isAuthenticated: false,
        auth_token: ''
    }

    const [state, dispatch] = useReducer(authReducer, initialState)


    const onLogin = async (email, password) => {
        setLoading(true)
        const data = {
            email: email,
            password: password,

        }

        await axios.post('http://127.0.0.1:8000/auth/token/login/', data)
            .then((response) => {
                console.log(response.data)
                localStorage.setItem('auth_token', response.data.auth_token)
                localStorage.setItem('isAuthenticated', true)
                //setAuthToken(localStorage.getItem('auth_token'))
                // if (localStorage.getItem('auth_token').length === 40) {
                //     setIsAuthenticated(true)
                // }
                dispatch({ type: 'LOGIN_SUCCESSFUL' })
                setLoading(false)
                window.location.href = 'dashboard/add-channel/'

            })
            .catch((error) => {
                console.log(error.data)
                setLoading(false)
            })

    }

    const checkAuth = async () => {

        return await axios.get('http://127.0.0.1:8000/auth/users/me/', {
            headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        })

    }

    const checkUserStatus = async () => {

        return await axios.get('http://127.0.0.1:8000/app/check-status/', {
            headers: {
                'Authorization': `Token ${state.auth_token}`
            }
        })


    }

    const getStats = async () => {

        return await axios.get('http://127.0.0.1:8000/app/stats/', {
            headers: {
                'Authorization': `Token ${state.auth_token}`
            }
        })


    }

   
    return <AuthContext.Provider
        value={{
            state,
            dispatch,
            onLogin,
            checkAuth,
            checkUserStatus,
            getStats           

        }}
    >
        {children}
    </AuthContext.Provider>


}

export default AuthContext