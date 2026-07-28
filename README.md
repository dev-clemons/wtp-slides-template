# WebTigerPython Slides Template 🐯📊

## Overview

This project provides a comprehensive template for creating interactive slide decks using Slidev, specifically designed for WebTigerPython presentations. The template integrates WebTigerPython as an embedded iframe, allowing for dynamic and engaging educational content.

## 🚀 Features

- **Slidev Integration**: Leverage the power of Slidev for modern, markdown-based presentations
- **WebTigerPython Embedding**: Seamlessly include interactive Python programming environments
- **Easy Deployment**: One-click GitHub Pages deployment
- **Responsive Design**: Slides look great on any device

## 🛠 Prerequisites

- Node.js (v14+ recommended)
- npm

## 🏁 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/tiger-jython/wtp-slides-template.git

# Navigate to project directory
cd wtp-slides-template

# Install dependencies
npm install
```

### Development

```bash
# Start development server
npm run dev

# Open in browser
# Visit http://localhost:3030
```

## 📝 Editing Slides

- Edit `slides.md` to modify slide content
- Use markdown and Slidev-specific syntax for rich presentations
- Embed WebTigerPython directly in slides

## 🌐 Deployment

Every push to `main` or a `feature/**` branch is automatically built and published to GitHub Pages by [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml):

- `main` deploys to the site root: 👉 https://dev-clemons.github.io/wtp-slides-template/
- Any `feature/<name>` branch deploys to its own subpath: `https://dev-clemons.github.io/wtp-slides-template/feature/<name>/`

This lets multiple decks (conference talks, courses, etc.) live as separate branches in one repo, each with its own persistent URL, instead of needing a separate repo per deck. See the current decks in this repo's branch list.

### Adding a new deck

1. Create a branch named `feature/<your-deck-name>`
2. Push it — the Action builds and publishes it automatically
3. It goes live at `.../feature/<your-deck-name>/`

### Setup notes for forks/clones

- GitHub Pages source must be set to **"Deploy from a branch"** → `gh-pages` → `/ (root)` under Settings → Pages. The default "GitHub Actions" source only supports one live deployment at a time and won't work with this per-branch setup.
- The workflow uses a per-branch `concurrency.group` (`pages-${{ github.ref_name }}`) so multiple branches can deploy in parallel without cancelling each other.
- The `main` deploy uses `clean-exclude` to protect other branches' `feature/` subfolders on `gh-pages` from being wiped out when the root gets rebuilt.

## 📚 Resources

- [Slidev Documentation](https://sli.dev/)
- [WebTigerPython](https://webtigerpython.ethz.ch/)
- [WebTigerPython Docs](https://docs.webtigerpython.ethz.ch/)
- [GitHub Pages](https://pages.github.com/)

---

**Happy Presenting!** 🎉👩‍💻👨‍💻