import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useErrorStore = defineStore('errorStore', () => {
    const errorMessage = ref('')
    const isErrorVisible = ref(false)

    const errorPageMessage = ref('')
    const errorPageStatus = ref(0)

    const setError = message => {
        errorMessage.value = message
        isErrorVisible.value = true
    }

    const clearError = () => {
        errorMessage.value = ''
        isErrorVisible.value = false
    }

    const setErrorPage = (status, message) => {
        errorPageMessage.value = message
        errorPageStatus.value = status
    }

    const clearErrorPage = () => {
        errorPageMessage.value = ''
        errorPageStatus.value = 0
    }

    return {
        errorMessage,
        isErrorVisible,
        errorPageMessage,
        errorPageStatus,
        setError,
        clearError,
        setErrorPage,
        clearErrorPage
    }
})