import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import { Navigate } from 'react-router'
import AuthContext from '../../context/AuthContext'
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import Sidebar from '../../components/Sidebar';



// const checkAuth = async () =>{

//   return await axios.get('http://127.0.0.1:8000/auth/users/me/',{
//    headers:{
//      'Authorization':`Token ${localStorage.getItem('auth_token')}`
//    }
//  })

// }

export default function Dashboard() {


  const { state, getStats } = useContext(AuthContext)

  const [percentage, setPercentage] = useState(0);

  const refreshStats = ()=>{
    getStats()
          .then(response => {
            setPercentage(JSON.parse(response.data).op_percentage.toFixed(2))
            localStorage.setItem('percentage', JSON.parse(response.data).op_percentage.toFixed(2))
          })
          .catch(error => {
            console.log(error.messsage)
          })
  }


  useEffect(() => {
    if (!state.auth_token) {

      <Navigate to={'/login'} />
    }
    else {

      // //  checkAuth()
      // //  .then(response => {

      // //   console.log(response.data)
      // //   //dispatch({type:'AUTH_STATUS'})

      // // })
      // // .catch(error=>{

      // //   console.log(error)
      // //  // dispatch({type:'LOGOUT'})

      // // })
      if (localStorage.getItem('percentage')) {
        setPercentage(localStorage.getItem('percentage'))
      } else {
        getStats()
          .then(response => {
            setPercentage(JSON.parse(response.data).op_percentage.toFixed(2))
            localStorage.setItem('percentage', JSON.parse(response.data).op_percentage.toFixed(2))
          })
          .catch(error => {
            console.log(error.messsage)
          })
      }
    }
    console.log('Session Fired')

  }, [])


  return (
    <div className='h-full w-full flex  items-center' >
      <Sidebar className='w-full' />
      <div className='flex w-full h-full flex-col items-center justify-center gap-4' >
       <div className='flex flex-col gap-4 justify-center items-center' >
       <CircularProgressbar
          value={percentage}
          text={`${percentage}%`}
          styles={buildStyles({

            rotation: 0.25,
            strokeLinecap: 'butt',
            textSize: '16px',
            pathTransitionDuration: 0.5,
            pathColor: `rgba(250, 105, ,${percentage / 100} )`,
            textColor: '#f88',
            trailColor: '#d6d6d6',
            backgroundColor: '#3e98c7',
          })}
        />

          <button
          onClick={()=>refreshStats()}
          className='px-2 py-1 hover:scale-125 transition ease-in-out duration-400 font-inter text-sm rounded bg-red-500 text-white outline-none' 
          > 
          Refresh 
          </button>
       </div>
      </div>
    </div>
  )
}
