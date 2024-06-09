<script setup lang="ts">
const year = new Date().getFullYear()

const links = [[{
    label: `${year} - Student Trainee Center`,
}],
[{
    label: 'Contact',
    icon: 'i-heroicons-envelope',
    to: 'mailto:martin.cernoch@studentstc.cz'
}]]
</script>

<template>
    <UDivider label="What the Code" />
    <UHorizontalNavigation :links="links" class="border-b border-gray-200 dark:border-gray-800 px-[320px]" />
</template>