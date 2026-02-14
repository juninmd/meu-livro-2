export default {
  lang: 'pt-BR',
  title: 'A Última Frequência',
  description: 'Livro distópico em capítulos',
  themeConfig: {
    nav: [
      { text: 'Início', link: '/' },
      { text: 'Capítulo 1', link: '/capitulo-1' },
      { text: 'Personagens', link: '/personagens' },
      { text: 'Universo', link: '/sobre' }
    ],
    sidebar: [
      {
        text: 'Leitura',
        items: [
          { text: 'Visão Geral', link: '/' },
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
}
