import React from 'react'
import { Link } from 'react-router-dom'
import { CiGrid31 } from 'react-icons/ci'

export default function PageNotFound() {
    return (
        <div className='h-full w-full flex items-center justify-center p-10' >

            <div className='flex gap-4 ' >
                <div className='flex flex-col gap-3 items-center justify-start' >
                    <h1 className='text-5xl font-bold' >404</h1>
                    <h2 className='text-xl' >Oooops</h2>
                    <CiGrid31 className='text-9xl' />
                    <h2 className='text-2xl' > Page Not Found </h2>
                    
                    <div>
                        <Link
                            className='px-2 py-1 mt-20 mx-auto font-inter text-sm rounded bg-red-500 text-white'
                        to={'/'}
                        >
                            Back to Home
                        </Link>
                    </div>
                </div>
                <div>
                   
                </div>
            </div>

        </div>
    )
}
