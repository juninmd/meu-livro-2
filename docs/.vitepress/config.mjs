import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'pt-BR',
  title: 'Protocolo Éden',
  description: 'Um thriller sci-fi distópico sobre sobrevivência, segredos e rebelião na estação orbital Éden.',
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: 'Capítulo 1', link: '/capitulo-1' },
      { text: 'Capítulo 2', link: '/capitulo-2' },
      { text: 'Personagens', link: '/personagens' },
      { text: 'Sobre', link: '/sobre' }
    ],
    sidebar: [
      {
        text: 'Leitura',
        items: [
          { text: 'Início', link: '/' },
          { text: 'Capítulo 1: Sombra Digital', link: '/capitulo-1' },
          { text: 'Capítulo 2: Ressonância', link: '/capitulo-2' },
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
