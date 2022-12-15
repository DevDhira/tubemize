import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

export default function Nav() {

  const { state, dispatch } = useContext(AuthContext)

  return (
    <div className='w-full flex justify-between px-4 py-3 shadow rounded-b-lg' >
     <div className='w-full flex items-center bg-ytred' >
                <h1 className='text-xl font-poppins font-bold text-ytred' > tubemize </h1>
            </div>
      <div className="flex justify-end gap-4 items-center w-full">
        <Link to={'/'} > Home </Link>
        <Link className='font-inter' to={'/login'} > Login </Link>
        <Link to={'/register'} > Register </Link>
   
        {/* <Link to={'/reset-password'} > Reset Password </Link>       */}


      </div>
    </div>
  )
}
