import axios from 'axios'
import React, { useEffect, useState } from 'react'
import {  useNavigate, useParams } from 'react-router'
import { InfinitySpin } from 'react-loader-spinner'
import {BsCheck2Circle} from 'react-icons/bs'
import { Link } from 'react-router-dom'

export default function PaymentSuccess() {

  const params = useParams()

  const navigate = useNavigate()
  

  const [loading, setLoading] = useState(false)

  const submitSession = async () => {

    setLoading(true)

    const data = {
      session_id: params.CHECKOUT_SESSION_ID
    }


    await axios.post('http://127.0.0.1:8000/stripe/session/', data,{
      headers: {
        'Authorization': `Token ${localStorage.getItem('auth_token')}` 
      }})
      .then((response) => {
        console.log(response.data)
        setLoading(false)
        window.location.href='/dashboard'
      })
      .catch((error) => {
        console.log(error.message)
        setLoading(false)
        //navigate('/welcome')
      })

  }


  useEffect(() => {

  submitSession()


  }, [params])


  return (
    <div className='h-screen w-full flex items-center justify-center ' >
      {loading
        ?
        <div className='flex flex-col gap-2 items-center' >
          <InfinitySpin
          width='200'
          color="red"
        />
        <h1> Processing Payment... </h1>
        </div>
        :
        <div className='flex flex-col gap-3 items-center' >
          <BsCheck2Circle className='text-8xl text-green-600' />
          <h1 className='text-lg font-semibold font-inter' >Your Payment is Successful </h1>
          <p className='w-3/4 text-center opacity-40 font-inter' > Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
          <Link
          to={'/dashboard'} 
          className='underline text-red-500 text-sm font-inter' 
          > 
          Back to Dashboard 
          </Link>
        </div>
      }
    </div>
  )
}
