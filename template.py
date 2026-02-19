import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')

project_name = "InNoteView"

list_of_files = [
    ".github/workflows/ci.yml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/custom_exceptions.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/site.py",
    f"src/{project_name}/youtube.py",
    "tests/__init__.py",
    "tests/test_site.py",
    "tests/test_youtube.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filename}")
    
    else:
        logging.info(f"{filename} already exists")