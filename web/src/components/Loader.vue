<script setup>
</script>

<template>
    <div class="loader">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
    </div>
</template>

<style scoped>
.loader {
    position: fixed;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: var(--color-main-bg);
    z-index: 10;
}

.dot {
    width: 16px;
    height: 16px;
    margin: 0 8px;
    border-radius: 50%;
    background-color: var(--color-primary);
    animation: bounce 0.6s infinite alternate;
}

.dot:nth-child(2) {
    animation-delay: 0.2s;
}

.dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes bounce {
    to {
        transform: translateY(-20px);
        opacity: 0.8;
    }
}
</style>