import tempfile
import os
import sys
import re

import app_logger

logger = app_logger.get_logger(__name__)

def setup_tmpdir():
    try:
        tmpdir = tempfile.TemporaryDirectory()
        tmpdir.name += "/output"
    except:
        logger.error("Failed to create temporary folder")
        sys.exit()
    
    return tmpdir

def setup_output_dir():
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "output")
    
    if os.path.exists(output_dir):
        asar_path = os.path.join(output_dir, 'app.asar')
        if os.path.exists(asar_path):
            try:
                os.remove(asar_path)
                logger.info("app.asar successfully deleted")
            except:
                logger.error(f"Failed to remove app.asar in {output_dir}")
                sys.exit()
    else:
        os.makedirs(output_dir)
        logger.info("Output directory successfully created")

def find_urls_in_file(file:str, find_by: str):
    url_pattern = re.compile(r'https?://[^\s\'"<>]+')
    links = [i for i in url_pattern.findall(file) if find_by in i]
    return links

def replace_urls_in_file(file: str, urls: list[str]):
    content = file
    for url in urls:
        new_url = input(f"Enter new url instead of {url}\n")
        logger.info(f"Replacing {new_url} instead of {url}")
        content = content.replace(url, new_url)
    return content
