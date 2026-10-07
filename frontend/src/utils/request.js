import axios from 'axios'

const instance = axios.create({
    baseURL: process.env.VUE_APP_API_BASE_URL || '/api',
    timeout: 60000
})

instance.interceptors.request.use(config => {
    const token = window.localStorage.getItem('token')
    if (token) config.headers.Authorization = `Bearer ${token}`
    return config
}, error => Promise.reject(error))

instance.interceptors.response.use(
    response => response.data,
    error => {
        if (error.response?.status === 401) {
            window.localStorage.removeItem('token')
            window.localStorage.removeItem('userId')
        }
        return Promise.reject(error)
    }
)

export function request(config) {
    return instance(config)
}


