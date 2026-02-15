import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'pt-BR',
  title: 'A Última Frequência',
  description: 'Uma distopia cyberpunk onde o som é proibido e a música é a revolução.',
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: 'Capítulo 1', link: '/capitulo-1' },
      { text: 'Personagens', link: '/personagens' },
      { text: 'Sobre', link: '/sobre' }
    ],
    sidebar: [
      {
        text: 'Leitura',
        items: [
          { text: 'Início', link: '/' },
          { text: 'Capítulo 1: O Sinal Fantasma', link: '/capitulo-1' },
          { text: 'Personagens', link: '/personagens' },
          { text: 'Sobre o Universo', link: '/sobre' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/juninmd/meu-livro-2' }
    ]
  }
})
