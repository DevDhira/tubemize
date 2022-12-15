import React, { useContext, useState } from 'react'
import AuthContext from '../context/AuthContext'

import { RiLoginCircleFill } from 'react-icons/ri'
import { Link } from 'react-router-dom'


export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  //const [loading, setLoading] = useState(false)

  const { onLogin, loading } = useContext(AuthContext)

  return (
    <div className='container h-full w-full flex' >
      <div className='h-full w-full bg-red-500' >

      </div>


      <div className='container h-full w-full p-5 flex flex-col gap-4 items-center justify-center' >

        <div className='w-3/4 mx-auto' >
          <div className='flex flex-col gap-4 my-10 justify-center items-center' >
            <RiLoginCircleFill className='text-5xl' />
            <h1 className='text-2xl font-semibold' > Hello Again ! 👋 </h1>
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
            <Link to={'/reset-password'} className='w-full text-end text-sm font-inter underline text-red-300' > Forgot Password? </Link>
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
                onClick={() => onLogin(email, password)}
              >
                Login
              </button>
            }

          </div>

        </div>


      </div>
    </div>
  )
}
