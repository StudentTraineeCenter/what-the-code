export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxt/content', '@nuxt/ui'],
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      script: [
        { src: 'https://kit.fontawesome.com/f6333c832d.js', defer: true, crossorigin: 'anonymous' },
      ],
      htmlAttrs: {
        lang: 'cs'
      }
    }
  }
})
