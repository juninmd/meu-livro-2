import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "A Última Frequência",
  description: "Uma distopia cyberpunk onde o som é proibido e a música é a revolução.",
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: 'Sobre', link: '/sobre' },
      { text: 'Personagens', link: '/personagens' },
      { text: 'Capítulo 1', link: '/capitulo-1' }
    ],
    sidebar: [
      {
        text: 'A História',
        items: [
          { text: 'Sobre o Universo', link: '/sobre' },
          { text: 'Personagens', link: '/personagens' }
        ]
      },
      {
        text: 'Capítulos',
        items: [
          { text: 'Capítulo 1: O Sinal Fantasma', link: '/capitulo-1' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/juninmd/meu-livro' }
    ]
  }
})
