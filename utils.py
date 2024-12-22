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

def replace_urls_in_file(file_path: str, find_by: str):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()

        file_name = os.path.split(file_path)[-1]

        logger.info(f"Replacing urls in {file_name}..")

        try:
            urls = find_urls_in_file(content, find_by)

            for url in urls:
                new_url = input(f"Enter new url instead of {url}\nNew url:")
                logger.info(f"Replacing {new_url} instead of {url}")
                content = content.replace(url, new_url)

            file.seek(0)
            file.write(content)
            file.truncate()

            logger.info(f"Successfully replacing urls in {file_name}!")
        except:
            logger.error(f"Failed replacing urls in {file_name}", exc_info=True)
            sys.exit()
        


