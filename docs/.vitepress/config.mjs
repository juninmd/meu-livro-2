import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'pt-BR',
  title: 'O Legado de Silício',
  description: 'Um thriller sci-fi/fantasia pós-apocalíptico onde Elara busca reacender o mundo à sombra de deuses-máquina.',
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: 'Capítulo 1', link: '/capitulos/capitulo-1' },
      { text: 'Capítulo 2', link: '/capitulos/capitulo-2' },
      { text: 'Capítulo 3', link: '/capitulos/capitulo-3' },
      { text: 'Capítulo 4', link: '/capitulos/capitulo-4' },
      { text: 'Personagens', link: '/personagens' },
      { text: 'Sobre', link: '/sobre' }
    ],
    sidebar: [
      {
        text: 'Leitura',
        items: [
          { text: 'Início', link: '/' },
          { text: 'Capítulo 1: O Canto', link: '/capitulos/capitulo-1' },
          { text: 'Capítulo 2: Relíquias', link: '/capitulos/capitulo-2' },
          { text: 'Capítulo 3: O Silêncio de Neon', link: '/capitulos/capitulo-3' },
          { text: 'Capítulo 4: Sombras e Sinapses', link: '/capitulos/capitulo-4' },
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
