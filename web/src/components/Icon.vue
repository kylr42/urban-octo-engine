<script setup>
import { defineAsyncComponent } from 'vue'

const props = defineProps({
    iconName: String
})

const icon = defineAsyncComponent(() => {
    return import(`@/assets/svg/${ props.iconName }.svg`)
})
</script>

<template>
    <component :is="icon"></component>
</template>