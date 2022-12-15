import React, { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router'

import { FidgetSpinner } from  'react-loader-spinner'
import modAxios from '../custom/CustomAxios'
//import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";



export default function Activation() {

    const params = useParams()
    const navigate = useNavigate()
    useEffect(() => {
      console.log(params)    
    
 
      const data = {
        uid:params.uid,
        token:params.token
      }    

      modAxios.post(`/auth/users/activation/`,data)
    .then((response)=>{
        console.log(response.data)
       navigate('/login')
    })
    .catch((error)=>{
        console.log(error)
       // alert('Something went wrong')
       navigate('/login')
    })
    
     // eslint-disable-next-line
    }, [params.uid, params.token])
    

  return (
    <div className='h-screen flex justify-center items-center' >
        <FidgetSpinner
  visible={true}
  height="80"
  width="80"
  ariaLabel="dna-loading"
  wrapperStyle={{}}
  wrapperClass="dna-wrapper"
  ballColors={['#ff0000', '#00ff00', '#0000ff']}
  backgroundColor="#F4442E"
/>
    </div>
  )
}
