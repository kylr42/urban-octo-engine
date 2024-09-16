<script setup>
import { useProductStore } from '@/stores/productStore.js'
import { useErrorStore } from '@/stores/errorStore'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import Loader from '@/components/Loader.vue'
import Icon from '@/components/Icon.vue'

const route = useRoute()
const router = useRouter()
const errorStore = useErrorStore()
const productStore = useProductStore()
const product = ref({
    name: '',
    price: ''
})

onMounted(async () => {
    try {
        await productStore.getProducts()
        isLoadingPage.value = false
    } catch (e) {
        isLoadingPage.value = false
        errorStore.setError('Не удалось загрузить данные')
    }
})

const isLoadingPage = ref(true)
const isLoading = ref(false)


const createProduct = async () => {
    isLoading.value = true

    if (!product.value.name || !product.value.price) {
        errorStore.setError('Заполните все поля')
        isLoading.value = false
        return
    }

    const requestBody = {
        name: product.value.name,
        price: product.value.price
    }
    
    await productStore.createProduct(requestBody)
    isLoading.value = false
}
</script>

<template>
    <Loader v-if="isLoadingPage"/>
    <section class="product">

        <div class="product_left flex-item">

            <div class="product_form card">
                <h2 class="product_form-title">Выберите банк получателя</h2>

                <div class="product_form-amount">
                    <input
                        type="text"
                        v-model.number="product.name"
                        class="input"
                    >
                </div>

                <button 
                    @click="createProduct"
                    :disabled="isLoading" 
                    class="button"
                >   
                    <span v-if="!isLoading">Создать заявку</span>
                    
                    <span v-else class="dots-loader">
                        <span class="dot"></span>
                        <span class="dot"></span>
                        <span class="dot"></span>
                    </span>
                </button>
            </div>

        </div>

    </section>
</template>

<style lang="scss" scoped>
.overlay {
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    z-index: 10;
    background: #00000050;
}

.modal {
    position: fixed;
    width: 340px;
    padding: 20px;
    border-radius: 16px;
    z-index: 12;
    background: var(--finish-color);
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    gap: 12px;
    align-items: center;
}

.modal_title {
    font-size: 20px;
    color: var(--color-text-primary);
    font-weight: 600;
}

.modal_body {
    font-size: 17px;
    text-align: center;
    color: var(--color-text-secondary);
}

.modal .button {
    width: 100%;
}

.dots-loader {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 40px;
}

.dot {
    background-color: white;
    border-radius: 50%;
    width: 8px;
    height: 8px;
    animation: bounce 1.4s infinite both;
}

.dot:nth-child(1) {
    animation-delay: -0.32s;  
}

.dot:nth-child(2) {
    animation-delay: -0.16s;
}

@keyframes bounce {
    0%, 80%, 100% {
        transform: scale(0);
    }
    40% {
        transform: scale(1);
    }
}

.product {
    display: flex;
    margin: 0 -10px;
}

.flex-item {
    flex: 0 0 50%;
    padding: 0 10px;
}

.card {
    border-radius: 16px;
}

.product_form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.product_form-title {
    text-align: center;
    color: var(--color-text-primary);
    font-weight: 600;
    font-size: 22px;
}

.banks {
    display: flex;
    flex-wrap: wrap;
    row-gap: 20px;
    margin: 0 -10px;
}

.banks_item {
    flex: 0 0 50%;
    padding: 0 10px;
}

.bank {
    height: 130px;
    background: var(--color-bg);
    color: var(--color-text-primary);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 16px;
    gap: 8px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.3s ease;

    &:hover {
        background: rgba(74, 144, 226, 0.3);
    }

    &.active {
        border: solid 2px var(--color-primary);
    }
}

.bank_logo {
    width: 40px;
    height: 40px;
}

.bank_label {
    font-weight: 600;
    color: var(--color-text-primary);
}


.input {
    border-radius: 16px;
    background: var(--color-bg);
    width: 100%;
    height: 50px;
    padding: 0 30px 0 20px;
    font-size: 18px;
    color: var(--color-text-primary);

    &:disabled {
        opacity: .9;
    }
}

.button {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
    background: #4A90E2;
    border-radius: 16px;
    color: #f5f5f5;
    font-weight: 600;
    font-size: 18px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;

    &.support {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;

        .icon {
            width: 24px;
            height: 24px;
            color: #f5f5f5;
        }
    }

    &:hover {
        background: darken(#4A90E2, 10%);
    }

    &:active {
        background: darken(#4A90E2, 15%);
        transform: scale(0.97);
    }
}

.product_right {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

@media (max-width: 768px) {
    .product {
        gap: 40px;
        flex-direction: column;
    }
} 

@media (max-width: 440px) {
    .bank_label {
        font-size: 14px;
    }

    .product_form-amount .icon {
        width: 20px;
        height: 20px;
    }

    .button {
        font-size: 16px;
    }

    .bank_logo {
        width: 30px;
        height: 30px;
    }
}
</style>