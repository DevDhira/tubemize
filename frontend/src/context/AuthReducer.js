const authReducer = (state, action) =>{
    switch(action.type){

        case 'LOGOUT':
            return {
                ...state,
                isAuthenticated:false,
                auth_token:''
            }
        
        case 'LOGIN_SUCCESSFUL':
                return {
                    ...state,
                    isAuthenticated:localStorage.getItem('auth_token')? true :false,
                    auth_token:localStorage.getItem('auth_token')
            }
        
        case 'AUTH_STATUS':
            return {
                ...state,
                isAuthenticated:localStorage.getItem('auth_token')? true :false,
                auth_token:localStorage.getItem('auth_token')
        }
        

        default:
            return state
    }
}

export default authReducer