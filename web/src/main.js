import './styles/main.scss'
import './styles/_variables.scss';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './routes'
import axios from './api/axios'

const app = createApp(App)

app.config.globalProperties.$axios = axios
app.use(createPinia())
app.use(router)

app.mount('#app')
