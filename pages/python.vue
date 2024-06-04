<template>
    <main class="my-16 xl:my-32">
        <div class="flex justify-center mb-6">
            <UBadge color="blue" variant="subtle" class="text-center">Lorem ipsum dolor sit amet!</UBadge>
        </div>
        <h1>Programování v Pythonu</h1>
        <div class="flex justify-center">
            <p class="black-text max-w-[840px] text-center my-4">Lorem ipsum dolor sit amet, consectetur adipiscing
                elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae congue mauris rhoncus
                aenean vel elit scelerisque mauris pellentesque. Amet nisl suscipit adipiscing bibendum est. Gravida
                arcu ac tortor dignissim convallis aenean et tortor at. Sapien eget mi proin sed libero enim sed.
            </p>
        </div>
        <div class="flex max-xl:flex-col gap-6 justify-center mt-6">
            <UButton class="flex justify-center" to="/" label="Přejít na domovskou stránku" color="blue" />
            <UButton class="flex justify-center" to="/python" label="Přejít na stránku s materiály na Python"
                color="blue" />
        </div>
        <ContentList path="/python" v-slot="{ list }">
            <div v-for="article in list" :key="article._path">
                <NuxtLink :to="`${article._path}`">
                    <UCard class="mt-24">
                        <template #header>
                            <h2>{{ article.title }}</h2>
                        </template>

                        <p class="text-center">{{ article.description }}</p>

                        <template #footer>
                            <div class="flex items-center justify-between">
                                <div class="flex gap-6 items-center">
                                    <UAvatar :src="`${article.avatar}`" alt="Avatar" />
                                    <p>{{ article.author }}</p>
                                </div>
                                <ULink :to="`${article._path}`" active-class="text-primary"
                                    inactive-class="text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200">
                                    Přečíst článek
                                </ULink>
                            </div>
                        </template>
                    </UCard>
                </NuxtLink>
            </div>
        </ContentList>
    </main>
</template>