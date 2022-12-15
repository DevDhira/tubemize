import React from 'react'
import { BsExclamationOctagon } from 'react-icons/bs'
import { Link } from 'react-router-dom'

export default function PaymentCancel() {
  return (
    <div>
      <div className='w-screen h-screen flex justify-center items-center py-5' >
        <div className='flex flex-col items-center gap-2' >
          <BsExclamationOctagon className='text-8xl text-red-500' />
          <h1 className='text-lg font-semibold font-inter' >😥 Payment Cancelled </h1>
          <p className='w-3/4 text-center opacity-40 font-inter' > Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
          <Link
            to={'/subscription'}
            className='underline text-red-500 text-sm font-inter'
          >
            Back to Subscriptions
          </Link>
        </div>
      </div>
    </div>
  )
}
