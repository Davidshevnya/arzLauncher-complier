from asarPy import pack_asar, extract_asar

import os
import sys

import app_logger
import utils

logger = app_logger.get_logger(__name__)
tmpdir = utils.setup_tmpdir()


def extract(path_to_file: str):
        logger.info(f"Extracting asar file in {tmpdir.name}")
        try:
            extract_asar(path_to_file, tmpdir.name)
            logger.info("Asar file successfully extracted")
        except:
              logger.error(f"Failed to extract asar file", exc_info=True)
              
def pack():
    utils.setup_output_dir()
    logger.info(f"Pack folder {tmpdir.name} into asar file")
    try:
        pack_asar(tmpdir.name, "output/app.asar")
    except:
        logger.error(f"Failed to pack folder into asar file", exc_info=True)


def change_links_in_files(launcher_type: int):
    if launcher_type not in [1,2,3]:
        logger.error("You entered an incorrect number.")
        sys.exit()

    find_by = ""

    if launcher_type == 1: # Korista
        find_by = "ko-rista"
    elif launcher_type == 2: # Suvorov
        find_by = "suvorov-company"
    else: # Orig arz
         find_by = "arz"

    logger.debug(f"Launcher type: {find_by}")
    bundle_js_path = os.path.join(tmpdir.name, "static/bundle.js")
    logger.info(f"Opening bundle.js of launcher for replacing urls (path: {bundle_js_path})")

    with open(bundle_js_path, 'r+', encoding="utf-8") as file:
        content = file.read()
        logger.info("Replacing urls in bundle.js..")

        try:
            urls = utils.find_urls_in_file(content, find_by)
            new_content = utils.replace_urls_in_file(content, urls)
            file.seek(0)
            file.write(new_content)
            file.truncate()

            logger.info("Successfully replacing urls in bundle.js!")
        except:
            logger.error("Failed replacing urls in bundle.js!", exc_info=True)
            sys.exit()