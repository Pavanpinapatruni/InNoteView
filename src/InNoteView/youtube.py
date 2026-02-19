"""
YouTube video rendering module for InNoteView package.

Provides functionality to embed YouTube videos directly
within Jupyter Notebook cells. Supports multiple YouTube URL formats.
"""

import re

from IPython.display import IFrame, HTML

from innoteview.logger import get_logger
from innoteview.custom_exception import InvalidYouTubeURLError

# Initialize logger for this module
logger = get_logger(__name__)

# Regex patterns for supported YouTube URL formats
YOUTUBE_PATTERNS = [
    # https://www.youtube.com/watch?v=VIDEO_ID
    r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
    # https://youtu.be/VIDEO_ID
    r'(?:https?://)?youtu\.be/([a-zA-Z0-9_-]{11})',
    # https://www.youtube.com/embed/VIDEO_ID
    r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})',
]


def _extract_video_id(url: str) -> str:
    """
    Extract the YouTube video ID from various URL formats.

    This is a private helper function (prefixed with _) that
    is not exposed to end users.

    Args:
        url (str): A YouTube video URL.

    Returns:
        str: The 11-character YouTube video ID.

    Raises:
        InvalidYouTubeURLError: If no valid video ID can be extracted.
    """

    for pattern in YOUTUBE_PATTERNS:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            logger.debug(f"Extracted video ID: {video_id} from URL: {url}")
            return video_id

    # No pattern matched
    logger.error(f"Could not extract video ID from URL: {url}")
    raise InvalidYouTubeURLError(url)


def render_youtube_video(
    url: str,
    width: int = 800,
    height: int = 450
) -> IFrame:
    """
    Embed a YouTube video inline within a Jupyter Notebook cell.

    Accepts multiple YouTube URL formats and automatically
    converts them to the embeddable format.

    Args:
        url (str): A YouTube video URL. Supported formats:
                   - https://www.youtube.com/watch?v=VIDEO_ID
                   - https://youtu.be/VIDEO_ID
                   - https://www.youtube.com/embed/VIDEO_ID
        width (int, optional): Width of the video frame in pixels.
                              Defaults to 800.
        height (int, optional): Height of the video frame in pixels.
                               Defaults to 450.

    Returns:
        IPython.display.IFrame: An IFrame object that Jupyter renders inline.

    Raises:
        InvalidYouTubeURLError: If the URL is not a valid YouTube URL.

    Example:
        >>> from innoteview import render_youtube_video
        >>> render_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        >>> render_youtube_video("https://youtu.be/dQw4w9WgXcQ", width=640, height=360)
    """

    # Step 1: Validate that url is a string
    if not isinstance(url, str):
        logger.error(f"URL must be a string. Received type: {type(url)}")
        raise InvalidYouTubeURLError(str(url))

    # Step 2: Extract the video ID (this validates the URL format too)
    video_id = _extract_video_id(url)

    # Step 3: Construct the embed URL
    embed_url = f"https://www.youtube.com/embed/{video_id}"

    # Step 4: Log the successful rendering attempt
    logger.info(
        f"Rendering YouTube video → ID: {video_id} "
        f"(width={width}, height={height})"
    )

    # Step 5: Create and return the IFrame
    return IFrame(src=embed_url, width=width, height=height)