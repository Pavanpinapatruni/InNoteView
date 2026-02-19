# 🔭 InNoteView

A lightweight Python library to render HTTPS websites and YouTube videos directly inside Jupyter Notebooks.

## 🎯 Why InNoteView?

As a Data Scientist, you often need to:
- Reference documentation while coding
- Watch tutorial videos alongside your notebook
- View live websites without switching tabs

**InNoteView brings all of that INTO your notebook.**

## 🚀 Installation

```bash
pip install innoteview
```

## 📖 Quick Start

### Render a Website
```python
from innoteview import render_site

render_site("https://docs.python.org")
```

### Embed a YouTube Video
```python
from innoteview import render_youtube_video

render_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

## 🛠️ Features

- ✅ Render any HTTPS website inline in Jupyter cells
- ✅ Embed YouTube videos with auto-formatting
- ✅ Works in Jupyter Notebook, JupyterLab, and Google Colab
- ✅ Lightweight — only depends on IPython
- ✅ Custom logging and error handling

## 📦 Supported Environments

| Environment | Supported |
|------------|-----------|
| Jupyter Notebook | ✅ |
| JupyterLab | ✅ |
| Google Colab | ✅ |

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Pavan Pinapatruni** — [@Pavanpinapatruni](https://github.com/Pavanpinapatruni)