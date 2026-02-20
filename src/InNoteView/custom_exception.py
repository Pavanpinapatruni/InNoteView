"""
Custom exception module for InNoteView package.

This module defines package-specific exceptions that provide
clear, meaningful error messages to users when something goes wrong.
"""


class InNoteViewError(Exception):
    """
    Base exception class for all InNoteView errors.

    All custom exceptions in this package inherit from this class,
    making it easy to catch any InNoteView-specific error:

    Example:
        try:
            render_site("invalid-url")
        except InNoteViewError as e:
            print(f"InNoteView error: {e}")
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class InvalidURLError(InNoteViewError):
    """
    Raised when an invalid or non-HTTPS URL is provided.

    Example:
        raise InvalidURLError("http://example.com")
    """

    def __init__(self, url: str) -> None:
        self.url = url
        message = (
            f"Invalid URL provided: '{url}'. "
            f"Only HTTPS URLs are supported. "
            f"Please provide a URL starting with 'https://'"
        )
        super().__init__(message)


class InvalidYouTubeURLError(InNoteViewError):
    """
    Raised when a URL is not a valid YouTube video URL.

    Example:
        raise InvalidYouTubeURLError("https://notYouTube.com/watch?v=123")
    """

    def __init__(self, url: str) -> None:
        self.url = url
        message = (
            f"Invalid YouTube URL: '{url}'. "
            f"Supported formats: \n"
            f"  - https://www.youtube.com/watch?v=VIDEO_ID\n"
            f"  - https://youtu.be/VIDEO_ID\n"
            f"  - https://www.youtube.com/embed/VIDEO_ID"
        )
        super().__init__(message)