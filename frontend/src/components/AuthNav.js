import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

export default function AuthNav() {

    const { state, dispatch } = useContext(AuthContext)

    const [plan, setPlan] = useState('')

    useEffect(() => {
        dispatch({ type: 'AUTH_STATUS' })
        console.log(state.auth_token)
        if (localStorage.getItem('auth_token') !== '') {
            check_status()
        }

        console.log('Nav Useffect Fired...')

    }, [dispatch, plan])


    const onLogout = async () => {

        console.log(localStorage.getItem('auth_token'))

        await axios.post('http://127.0.0.1:8000/auth/token/logout/', {}, {
            headers: {
                Authorization: `Token ${localStorage.getItem('auth_token')}`
            }
        })
            .then((response) => {

                console.log(response)
                localStorage.removeItem('auth_token')
                localStorage.removeItem('isAuthenticated')
                localStorage.removeItem('percentage')
                dispatch({ type: 'LOGOUT' })


            })
            .catch((error) => {

                console.log(error.message)
                //  dispatch({type:'LOGOUT'})

            })

    }

    const check_status = async () => {



        await axios.get(`http://127.0.0.1:8000/stripe/status/`, {
            headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        }).then((response) => {
            console.log(response.data.plan)
            setPlan(response.data.plan)

        }).catch((error) => {
            console.log(error.message)
        })
    }

    const cancelSubscription = async () => {

        await axios.get(`http://127.0.0.1:8000/stripe/cancel/`, {
            headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        }).then((response) => {
            console.log(response.data)
            check_status()

        }).catch((error) => {
            console.log(error.message)
        })

    }

    return (
        <div className='w-full flex justify-between px-4 py-2 shadow rounded-b-lg' >
            <div className='w-full flex items-center bg-ytred' >
                <h1 className='text-xl font-poppins font-bold text-ytred' > tubemize </h1>
            </div>
            <div className="flex justify-end items-center w-full">

                {/* <Link to={'/dashboard'} > Dashboard </Link>
                <Link to={'/dashboard/add-channel'} > Add Channel </Link> */}
                {(state.auth_token !== '') && (
                    <div className="flex gap-4 items-center">
                        <button
                            onClick={() => {
                                onLogout()

                            }}
                            className='px-2 py-1 rounded bg-red-500 text-white font-inter'
                        >
                            Logout
                        </button>

                        {plan === 'free' ?

                            (<Link to={'/subscription'}
                                className='px-2 py-1 font-inter rounded bg-green-600 text-white'
                            >
                                Upgrade
                            </Link>) :
                            <button 
                            onClick={()=>cancelSubscription()}
                            className='px-2 py-1 font-inter rounded bg-red-500 text-white' 
                            >
                                Cancel Subscription
                            </button>

                        }




                    </div>
                )}


            </div>
        </div>
    )
}
