<script setup lang="ts">
useSeoMeta({
  title: 'What the Code',
  ogTitle: 'What the Code',
  description: 'What the Code.'
})
</script>

<template>
  <TheNav />
  <UContainer class="min-height">
    <NuxtPage />
  </UContainer>
  <TheFooter />

  <UNotifications />
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

:root {
  --blue-primary: #1e88e5;
  --black: #3a3a3a;
}

* {
  font-family: 'Poppins', sans-serif;
}

h1 {
  font-size: 48px;
  text-align: center;
  color: var(--black);
}

h2 {
  font-size: 32px;
  color: var(--blue-primary);
  text-align: center;
  margin-top: 32px;
  margin-bottom: 16px;
}

footer {
  background-color: var(--blue-primary);
  color: #ffffff;
  padding: 12px;
}

.black-text {
  color: var(--black);
}

.min-height {
  min-height: 100vh;
}

@media screen and (min-width: 1280px) {

  h1 {
    font-size: 92px;
  }

  h2 {
    font-size: 48px;
  }
}
</style>