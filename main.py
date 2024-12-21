import os
import sys

import app_logger
import asar

logger = app_logger.get_logger(__name__)

def main(path_to_file):
    if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
        logger.info(f"Asar file path: {os.path.realpath(path_to_file)}")
        asar.extract(os.path.realpath(path_to_file))
        asar.pack()
    else:
        logger.error(f"Asar file was not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <path_to_app_asar>")
    else:
        main(sys.argv[1])
        

