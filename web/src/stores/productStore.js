import { defineStore } from 'pinia'
import { ref } from 'vue'
import { useErrorStore } from './errorStore'
import { useRouter } from 'vue-router'
import axios from '@/api/axios'

export const useProductStore = defineStore('productStore', () => {
    const errorStore = useErrorStore()
    const router = useRouter()
    
    const productData = ref(null)

    const createProduct = async (requestBody) => {
        try {
            const { data } = await axios.post(`/api/v1/products`, requestBody)
            productData.value = data
        }

        catch (err) {
            if (err.response) {
                const status = err.response.status
                switch (status) {
                    case 422: 
                        errorStore.setError('Ошибка валидации, убедитесь в том, что все заполнено верно')
                        break
                    case 500:
                        errorStore.setError('Внутренняя ошибка, попробуйте позже')
                        break
                    default:
                        errorStore.setError('Неизвестная ошибка, попробуйте позже')
                }
            } 
            else if (err.request) {
                errorStore.setError('Сервер временно не отвечает, попробуйте позже')
            } 
            else {
                console.log('Ошибка в настройке запроса')
            }

            console.log(err)
        }
    }

    const getProducts = async () => {
        try {
            const { data } = await axios.get(`/api/v1/products/`)
            productData.value = data
        } 
        
        catch (err) {
            if (err.response) {
                const status = err.response.status
                switch(status) {
                    case 500:
                        errorStore.setErrorPage(500, 'Внутренняя ошибка, попробуйте позже')
                        break
                    default: 
                        errorStore.setErrorPage(0, 'Неизвестная ошибка, обратитесь в техническую поддержку')
                }
            }
            else if (err.request) {
                errorStore.setErrorPage(0, 'Сервер временно не отвечает, попробуйте позже')
            }
            else {
                console.log('Ошибка в настройке запроса')
            }
            console.log(err)
        }
    }

    return { productData, createProduct, getProducts }
})