import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s:")
project_name="cnn-classifier"

list_of_files= [
    f".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, file = os.path.split(filepath)
    if filedir!="":
        logging.info(f"Creating filedirectory: {filedir} for file: {file}")
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created filedirectory: {filedir} for file: {file}")

    if (not os.path.exists(file)) or (os.path.getsize(file))==0:
        logging.info(f"Creating empty file: {file} for filepath: {filepath}")
        open(filepath,"wb")
        logging.info(f"Created file: {file} for filepath: {filepath}")
    else:
        logging.info(f"{file} already exists")