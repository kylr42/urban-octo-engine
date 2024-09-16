<script setup>
import Error from '@/components/Error.vue'
</script>

<template>
    <div class="layout">
        <div class="layout_container">
            <Error />
            <slot />
        </div>
    </div>
</template>

<style lang="scss" scoped>
.layout {
    min-height: 100vh;
    background: var(--color-main-bg);
}

.layout_container {
    max-width: 900px;
    padding: 50px 20px 20px 20px;
    margin: 0 auto;
}
</style>