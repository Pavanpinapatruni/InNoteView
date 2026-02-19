"""
InNoteView - Render websites and YouTube videos inside Jupyter Notebooks.

A lightweight Python library designed for Jupyter Notebook
users. Seamlessly render HTTPS websites and embed YouTube videos directly
within .ipynb cells.

Quick Start:
    >>> from innoteview import render_site, render_youtube_video
    >>> render_site("https://docs.python.org")
    >>> render_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
"""

# These imports make functions available at the package leve
from innoteview.site import render_site
from innoteview.youtube import render_youtube_video

# WITHOUT these imports, users would have to write:
#   from innoteview.site import render_site        ← Longer, ugly
#
# WITH these imports, users can write:
#   from innoteview import render_site              ← Clean, simple!


__version__ = "0.0.1"

__all__ = [
    "render_site",
    "render_youtube_video",
]