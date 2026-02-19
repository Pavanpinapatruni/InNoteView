"""
Logging module for InNoteView package.

Provides centralized, consistent logging across all modules.
Uses Python's built-in logging library — no external dependencies.
"""

import logging


def get_logger(module_name: str) -> logging.Logger:
    """
    Create and return a configured logger for a given module.

    Each module gets its own named logger, which helps identify
    where log messages are coming from.

    Args:
        module_name (str): The name of the module requesting the logger.
                          Typically passed as __name__.

    Returns:
        logging.Logger: A configured logger instance.

    Example:
        from innoteview.logger import get_logger
        logger = get_logger(__name__)
        logger.info("This is an info message")
    """

    # Create a logger with the module's name
    logger = logging.getLogger(module_name)

    # Set the minimum logging level
    # DEBUG < INFO < WARNING < ERROR < CRITICAL
    logger.setLevel(logging.DEBUG)

    # Prevent adding duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        # Create a console handler (outputs to terminal/notebook)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Define the log message format
        formatter = logging.Formatter(
            fmt="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Attach the formatter to the handler
        console_handler.setFormatter(formatter)

        # Attach the handler to the logger
        logger.addHandler(console_handler)

    return logger