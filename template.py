import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# logging.info("Hello everyone! Welcome to the course")

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb',
    'app.py'
]

for filepath in list_of_files:
    
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Created directory {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file {filepath}")
    
    else:
        logging.info(f"File {filename} already exists")

