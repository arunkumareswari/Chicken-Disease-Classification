import os 
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, 
    format = '[%(asctime)s]: %(message)s:'
)

list_of_files = [
    ".github/workflow/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/cofig/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath)                    # object creation  --> Path is a class
    filedir, filename = os.path.split(filepath)  # os is a module, os.path is a sub-module and split() is a function

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creatiing directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty files: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
