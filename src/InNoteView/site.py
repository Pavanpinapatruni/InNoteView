"""
Site rendering module for InNoteView package.

Provides functionality to render HTTPS websites directly
within Jupyter Notebook cells using IPython's IFrame display.
"""

from IPython.display import IFrame

from innoteview.logger import get_logger
from innoteview.custom_exception import InvalidURLError

# Initialize logger for this module
logger = get_logger(__name__)


def render_site(
    url: str,
    width: int = 1024,
    height: int = 600
) -> IFrame:
    """
    Render an HTTPS website inline within a Jupyter Notebook cell.

    Args:
        url (str): The HTTPS URL of the website to render.
                   Must start with 'https://'.
        width (int, optional): Width of the rendered frame in pixels.
                              Defaults to 1024.
        height (int, optional): Height of the rendered frame in pixels.
                               Defaults to 600.

    Returns:
        IPython.display.IFrame: An IFrame object that Jupyter renders inline.

    Raises:
        InvalidURLError: If the URL is not a valid HTTPS URL.

    Example:
        >>> from innoteview import render_site
        >>> render_site("https://docs.python.org")
        >>> render_site("https://pandas.pydata.org", width=800, height=400)
    """

    # Validate that url is a string
    if not isinstance(url, str):
        logger.error(f"URL must be a string. Received type: {type(url)}")
        raise InvalidURLError(str(url))

    # Validate that url starts with https://
    if not url.startswith("https://"):
        logger.error(f"Invalid URL provided: {url}")
        raise InvalidURLError(url)

    # Log the successful rendering attempt
    logger.info(f"Rendering site → {url} (width={width}, height={height})")

    # Create and return the IFrame
    return IFrame(src=url, width=width, height=height)