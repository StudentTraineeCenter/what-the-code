<script setup lang="ts">
const isOpen = ref<boolean>(false)
</script>

<template>
    <UButton @click="isOpen = !isOpen" block label="Zobrazit řešení" class="mt-16" />
    <div v-if="isOpen === true">
        <ContentSlot :use="$slots.default" unwrap="p" />
    </div>
</template>