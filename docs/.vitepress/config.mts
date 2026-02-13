import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "O Legado de Silício",
  description: "Uma aventura épica em um mundo esquecido.",
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: 'Sobre', link: '/sobre' },
      { text: 'Capítulo 1', link: '/capitulo-1' }
    ],
    sidebar: [
      {
        text: 'O Livro',
        items: [
          { text: 'Sobre a Obra', link: '/sobre' },
          { text: 'Capítulo 1: O Despertar da Ruína', link: '/capitulo-1' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/juninmd/meu-livro' }
    ]
  }
})
