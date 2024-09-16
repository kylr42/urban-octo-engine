<script setup>
import Icon from '@/components/Icon.vue'
import { useErrorStore } from '@/stores/errorStore'
const error = useErrorStore()

const clearError = () => error.clearError()
</script>

<template>
    <div v-if="error.isErrorVisible" class="alert error">
        <div class="alert_left">
            <span class="alert_message error">{{ error.errorMessage }}</span>
        </div>

        <button class="button">
        </button>
    </div>
</template>

<style lang="scss" scoped>
.alert {
    position: fixed;
    max-width: 350px;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px;
    background: #fff;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;

    &.error {
        border: 1px solid var(--color-error);
        background: var(--color-error);
    }
}

.alert_left {
    display: flex;
    align-items: center;
    gap: 16px;
}

.icon-type {
    width: 40px;
    height: 40px;

    &.icon-error { color: var(--color-error); }
}

.button {
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}

.icon {
    width: 30px;
    height: 30px;
    
    &.error { fill:#fff; }
}

.alert_message {
    font-weight: 500;
    font-size: 13px;

    &.error { color: #fff; }
}

@media (max-width: 768px) {
    .alert {
        max-width: calc(100% - 40px);
        left: 20px;
        transform: translateX(0);
    }
} 
</style>
