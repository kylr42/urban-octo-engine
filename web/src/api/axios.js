import axios from 'axios'

const instance = axios.create({
    baseURL: import.meta.env.VITE_APP_BACKEND_URL,
    timeout: 15000,
  })
export default instance