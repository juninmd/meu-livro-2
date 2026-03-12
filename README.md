# 📖 Meu Livro 2 - Documentation & Content System

![VitePress](https://img.shields.io/badge/docs-VitePress-blue.svg)
![Python Scripts](https://img.shields.io/badge/automation-Python-green.svg)
![Status](https://img.shields.io/badge/status-in%20progress-yellow.svg)

**Meu Livro 2** é um sistema de documentação e criação de conteúdo estruturado, utilizando **VitePress** para a interface de leitura e scripts **Python** para automação de mídia e verificação de integridade.

---

## ✨ Recursos Principais

*   📚 **Leitura Moderna:** Interface limpa e responsiva baseada em VitePress.
*   🖼️ **Automação de Mídia:** Scripts integrados para geração de imagens via IA (DALL-E, Stable Diffusion).
*   🧪 **Verificação de Capítulos:** Sistema de validação por screenshots e scripts Python para garantir a qualidade do conteúdo.
*   ⚡ **Build Rápido:** Workflow otimizado para desenvolvimento e visualização instantânea.
*   🛠️ **Organização Modular:** Estrutura clara dividida entre documentação (docs), scripts e assets.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
| :--- | :--- |
| **Documentação** | [VitePress](https://vitepress.dev/) |
| **Automação** | Python 3.x |
| **Media Gen** | OpenAI DALL-E / Stable Diffusion Scripts |
| **JS Engine** | Node.js / pnpm |

---

## 🚀 Como Iniciar

### Pré-requisitos

*   Node.js (v18+)
*   Python (v3.10+)

### Instalação

```bash
# Clone o repositório
git clone git@github.com:juninmd/meu-livro-2.git

# Instale dependências Node
npm install

# Instale dependências Python (opcional, para scripts de mídia)
pip install -r scripts/requirements.txt
```

### Comandos de Documentação

```bash
# Iniciar modo de desenvolvimento
npm run docs:dev

# Gerar build estático
npm run docs:build

# Preview do build
npm run docs:preview
```

---

## 📂 Estrutura do Projeto

```text
meu-livro-2/
├── docs/               # Conteúdo Markdown do livro
├── scripts/            # Automação de imagens e verificação
│   ├── generate_*.py   # Geração de mídia via IA
│   └── verify_*.py     # Validação de capítulos
├── .github/            # Workflows de CI/CD
└── public/             # Ativos estáticos e imagens do livro
```

---

## 🧪 Verificação & Qualidade

O projeto utiliza screenshots de verificação para acompanhar o progresso dos capítulos. Veja a pasta raiz para arquivos como `verification_chapter_15.png` que validam o estado visual do projeto.

---

## 🤝 Contribuição

Para contribuir:
1. Revise as diretrizes no [AGENTS.md](./AGENTS.md).
2. Siga o fluxo de trabalho sugerido no [ROADMAP.md](./ROADMAP.md).
3. Abra um Pull Request detalhando suas alterações.

---

## 📄 Licença

Distribuído sob a licença **ISC**.

---

*"Writing is the ultimate form of thinking. Build the foundation, inspire the reader."*
