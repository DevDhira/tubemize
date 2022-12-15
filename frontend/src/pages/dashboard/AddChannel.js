import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import { Navigate, useNavigate } from 'react-router'
import Sidebar from '../../components/Sidebar'
import AuthContext from '../../context/AuthContext'

export default function AddChannel() {
    const { state, checkAuth, checkUserStatus } = useContext(AuthContext)

    const navigate = useNavigate()

    const [channelId, setChannelId] = useState('')

    const submitChannel = () => {

        const data = {
            channel_id: channelId,
        }

        axios.post(`http://127.0.0.1:8000/app/add-channel/`, data, {
            headers: {
                'Authorization': `Token ${state.auth_token}`
            }
        })
            .then(response => {
                console.log(response.data)
                navigate('/dashboard')
            })
            .catch((error) => {
                console.log(error)
            })

        setChannelId('')

    }

    useEffect(() => {

        if (!state.auth_token) {
            <Navigate to={'/login'} />
        }
        // else {

        //     checkAuth()
        //         .then(response => {
        //             console.log(response.data)                   
        //             //dispatch({type:'AUTH_STATUS'})      
        //         })
        //         .catch(error => {
        //             console.log(error)
        //             // dispatch({type:'LOGOUT'})      
        //         })

        // }
        else {
            checkUserStatus().then(response => {
                if (response.data.message === 'true') {
                    navigate('/dashboard')
                }


            }).catch(error => {
                console.log(error)
            })

        }

    }, [state])


    return (
        <div className='h-full w-full flex justify-center items-center' >
            <Sidebar className='w-full' />
            <div className='flex h-full w-full flex-col gap-3 justify-center items-center' >
                <div className='w-auto flex flex-col gap-3' >
                    <input
                        value={channelId}
                        onChange={(e) => { setChannelId(e.target.value) }}
                        type='text'
                        className='px-2 py-2 border font-inter text-sm text-slate-500 outline-none focus:ring ring-red-200 rounded'
                        placeholder='Your Youtube Id : UCE4RES-YPudggCh-IxlLk5A'
                    />

                    <button
                        onClick={() => submitChannel()}
                        className='px-2 py-1 text-white font-inter text-sm bg-red-600 rounded'

                    >
                        Add Channel

                    </button>
                </div>
            </div>
        </div>
    )
}
