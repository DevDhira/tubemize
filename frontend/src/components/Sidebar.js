import React from 'react'
import { CiViewTimeline,CiSquarePlus,CiCreditCardOff } from "react-icons/ci";
import { Link } from 'react-router-dom';


export default function Sidebar() {
    return (
        <div className='h-full w-6 bg-red-500 px-7 py-4  flex flex-col gap-4 items-center'  >
            <div className='rounded bg-ytred-500' >
            <Link to={'/dashboard'} >  <CiViewTimeline className='text-3xl font-bold text-white' /> </Link>
            </div>
            <div className='rounded bg-ytred-500' >
            <Link to={'/dashboard/add-channel'} >  <CiSquarePlus className='text-3xl font-bold text-white' /></Link>
            </div>
         
        </div>
    )
}
