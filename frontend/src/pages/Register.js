import React, { useState } from 'react'
import modAxios from '../custom/CustomAxios'

import { RiDoorLockLine } from 'react-icons/ri'
import { Link } from 'react-router-dom'


export default function Register() {

    const [email, setEmail] = useState('')
    const [notification, setNotification] = useState('')
    const [password, setPassword] = useState('')
    const [rePassword, setRePassword] = useState('')
    const [loading, setLoading] = useState(false)

    const onRegister = () => {
        setLoading(true)
        const data = {
            email: email,
            password: password,
            re_password: rePassword
        }


        modAxios.post(`/auth/users/`, data)
            .then((response) => {
                console.log(response.data)
                setLoading(false)
                setNotification('Verification Email Sent !')
            })
            .catch((error) => {
                console.log(error)
                setLoading(false)
            })

    }

    return (
        <div className='container h-full w-full flex ' >

            <div className='container h-full w-full p-5 flex flex-col gap-4 items-center justify-center' >

                <div className='w-3/4 mx-auto' >
                    <div className='flex flex-col gap-4 my-10 justify-center items-center' >
                        <RiDoorLockLine className='text-5xl' />
                        <h1 className='text-2xl font-semibold' > Welcome ! 🤝 </h1>
                        <p className='text-center opacity-50' > Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quaerat sunt provident suscipit dicta. Harum, ex. </p>

                    </div>
                    <div className='flex flex-col gap-4 justify-center items-center' >
                        <input
                            type="text"
                            className='w-full px-2 py-2 rounded border outline-none'
                            placeholder='Email'
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                        <input
                            type="password"
                            className='w-full px-2 py-2 rounded border outline-none'
                            placeholder='Password'
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <input
                            type="password"
                            className='w-full px-2 py-2 rounded border outline-none'
                            placeholder='Confirm Password'
                            value={rePassword}
                            onChange={(e) => setRePassword(e.target.value)}
                        />

<Link to={'/login'} className='w-full text-end text-sm font-inter underline text-red-300' > Already Have Account? </Link>

                        {loading ?

                            <button type="button"
                                className="inline-flex items-center justify-center px-2 py-2 w-full rounded bg-blue-500 text-white"
                                disabled="">
                                <svg className="w-5 h-5 mr-3 -ml-1 text-white animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none"
                                    viewBox="0 0 24 24">
                                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                    <path className="opacity-75" fill="currentColor"
                                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                    </path>
                                </svg>
                            </button>
                            :
                            <button
                                type="submit"
                                className='px-2 py-2 w-full rounded bg-red-500 text-white'
                                onClick={() => onRegister()}
                            >
                                Register
                            </button>
                        }

                    </div>

                </div>


            </div>
            <div className='h-full w-full bg-red-500' >

            </div>
        </div>
    )
}
