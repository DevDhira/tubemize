import React, { useState } from 'react'
import modAxios from '../custom/CustomAxios'
import { RiKey2Line } from 'react-icons/ri'
import { Link } from 'react-router-dom'
import {toast} from 'react-toastify'


export default function ResetPassword() {

    const [email, setEmail] = useState('')
    const [notification, setNotification] = useState('')
    const [loading, setLoading] = useState(false)



    const onSumbit = () => {
        setLoading(true)
        const data = {
            email: email,
        }

        modAxios.post(`/auth/users/reset_password/`, data)
            .then((response) => {
                console.log(response.data)
                setLoading(false)
                toast.success('🦄 Confirmation Email Sent !', {
                    position: "top-right",
                    autoClose: 500,
                    hideProgressBar: true,
                    closeOnClick: true,
                    pauseOnHover: true,
                    draggable: true,
                    progress: undefined,
                    theme: "light",
                    });
               
            })
            .catch((error) => {
                console.log(error)
                setLoading(false)
            })

    }

    return (
        <div className='w-full h-screen flex justify-center items-start py-10' >
            <div className='flex flex-col gap-3 items-center' >

                <div className="flex p-3 shadow  rounded-full">
                    <RiKey2Line className='text-center text-4xl text-red-500 ' />

                </div>

                <h1 className='font-inter text-xl font-bold text-center' > Forgot Password ?  </h1>
                <p className='text-sm font-inter' > No problem , we'll send you the reset link ! </p>
                <input
                    type="text"
                    className='w-full  px-1 py-1 rounded border text-sm font-inter outline-none text-slate-500'
                    placeholder='Email'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                {loading ?


                    <button type="button"
                        className="inline-flex items-center justify-center px-2 py-2 w-full rounded bg-blue-500 text-white"
                        disabled="">
                        <svg className="w-5 h-5 mr-3 -ml-1 text-white animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24">
                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                            <path className="opacity-75" fill="currentColor"
                                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                            </path>
                        </svg>

                    </button>
                    :
                    <button
                        type="submit"
                        className='px-2 py-2 w-full font-inter text-sm rounded bg-red-500 text-white'
                        onClick={() => onSumbit()}
                    >
                        Reset Password
                    </button>
                }
                <Link to={'/login'} className='font-inter underline text-sm text-red-500' > Back to log in </Link>
            </div>
            <h1 className='my-10 text-green-600' > {notification} </h1>
        </div>
    )
}
