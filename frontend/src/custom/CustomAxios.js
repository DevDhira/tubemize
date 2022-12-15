import axios from "axios";

const modAxios = axios.create({
    baseURL: process.env.REACT_APP_BASE_URL
})

if (localStorage.getItem('auth_token')){
    modAxios.defaults.headers.common['Authorization'] =`Token ${localStorage.getItem('auth_token')}`
}
else{
    modAxios.defaults.headers.common['Authorization'] =``
}

export default modAxios