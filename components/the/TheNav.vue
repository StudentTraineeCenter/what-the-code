<script setup lang="ts">
const links =
    [{
        label: 'Domů',
        icon: 'i-heroicons-home',
        to: '/'
    },
    {
        label: 'Python',
        icon: 'i-heroicons-code-bracket',
        to: '/python'
    }]
</script>

<template>
    <UHorizontalNavigation :links="links" class="border-b border-gray-200 dark:border-gray-800" />
</template>