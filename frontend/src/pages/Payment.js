import axios from 'axios'
import React from 'react'

export default function Payment() {


    const checkout = async (plan) => {

        const data = {
            plan: plan
        }

        await axios.post(`${process.env.REACT_APP_BASE_URL}/stripe/checkout/`, data, {
            headers: {
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        }).then((response)=>{

            console.log(response.data)
            window.location.href = response.data.url
        }).catch((error)=>{
            console.log(error.response.data)
        })


    }


    return (
        <>

            {/* <div className='p-5 w-full' >
                <h1 className='my-10 text-center text-2xl font-bold' >Subscription</h1>
            </div>

            <div className='p-10 w-full flex justify-evenly items-center' >
                <div className='p-5 rounded shadow flex flex-col gap-3 items-center' >
                    <h2 className='text-xl font-bold'>Basic Plan</h2>
                    <img className='h-52' alt='basic' src='https://img.freepik.com/free-vector/subscriber-concept-illustration_114360-3453.jpg?t=st=1654685116~exp=1654685716~hmac=b67fdd003003bc4f477b5184b2201a36a5a88ebefc2552ee7f4f723a2acef85f&w=740'></img>

                    
                       
                        <button 
                        onClick={()=>checkout('basic')}
                        className="px-2 py-2 bg-yellow-400 text-black rounded"                       
                        >
                        $100/month 
                        </button>
                    
                </div>
                <div className='p-5 rounded shadow flex flex-col gap-3 items-center' >
                    <h2 className='text-xl font-bold'>Premium Plan</h2>
                    <img className='h-52' alt='premium' src='https://img.freepik.com/free-vector/subscriber-concept-illustration_114360-2949.jpg?t=st=1654651458~exp=1654652058~hmac=fc1ea117f4198608284f1fea2f5af8f4c50f75692b80c711ad5c93793d0f3ab0&w=740'></img>
                        
                        <button
                            onClick={() => checkout('premium')}
                            className="px-2 py-2 bg-yellow-400 text-black rounded"
                        >
                            $200/month
                        </button>
                
                </div>
            </div> */}
       
       
       
        <div className='h-full w-full' >
            <div className='w-3/4 h-full mx-auto p-10 flex flex-col gap-3 items-center' >
                <h1 className='text-3xl font-bold font-inter underline text-red-500' > Ready to Get Started ! </h1>
                <h3 className='text-md font-inter text-center opacity-40 w-3/4' > Lorem ipsum, dolor sit amet consectetur adipisicing elit.</h3>
                <div className='w-4/5 my-10 mx-auto flex gap-7 justify-center' >
                    <div className='p-10 rounded shadow shadow-red-200 flex flex-col gap-4 w-full' >
                        <h1 className='text-2xl w-full flex gap-3 items-baseline font-inter' > <p className='text-5xl' >😺</p> Basic </h1>
                        <h1 className='flex items-baseline gap-2' > <strong className='text-4xl font-inter font-bold' >$100</strong>  <p className='font-inter font-light' >per month</p></h1>
                        <button
                        onClick={()=>checkout('basic')} 
                        className='my-3 px-3 py-2 bg-red-500 text-white rounded font-inter' 
                        > 
                        Get Started 
                        </button>
                        <h1 className='text-xl font-semibold' > Features </h1>
                        <div className='flex flex-col gap-3' >
                            <ul className='list-disc' >
                            <li className='text-lg font-semibold' > Lorem, ipsum. </li>
                            <li className='text-lg font-semibold' > Lorem, ipsum. </li>
                           
                            </ul>
                        </div>
                    </div>
                    <div className='p-10 rounded shadow shadow-red-200 flex flex-col gap-4 w-full' >
                    <h1 className='text-2xl w-full flex gap-3 items-baseline font-inter' > <p className='text-5xl' >🐱‍💻 </p> Premium </h1>
                        <h1 className='flex items-baseline gap-2' > <strong className='text-4xl font-inter font-bold' >$200</strong>  <p className='font-inter font-light' >per month</p></h1>
                        <button
                        onClick={() => checkout('premium')}
                        className='my-3 px-3 py-2 bg-red-500 text-white rounded font-inter' 
                        > 
                        Get Started 
                        </button>
                        <h1 className='text-xl font-semibold' > Features </h1>
                        <div className='flex flex-col gap-3' >
                            <ul className='list-disc' >
                            <li className='text-lg font-semibold' > Lorem, ipsum. </li>
                            <li className='text-lg font-semibold' > Lorem, ipsum. </li>
                            <li className='text-lg font-semibold' > Lorem, ipsum. </li>
                            <li className='text-lg font-semibold' > Lorem, ipsum. </li>
                           
                            </ul>
                        </div>
                    </div>
                   
                    
                </div>
               
            </div>
        </div>



        </>
    )
}
