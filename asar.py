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
    
   

    main_css_path = os.path.join(tmpdir.name, "static/main.css")
    bundle_js_path = os.path.join(tmpdir.name, "static/bundle.js")

    utils.replace_urls_in_file(main_css_path, find_by)
    utils.replace_urls_in_file(bundle_js_path, find_by)

def change_start_game_method():
    logger.info("Changing startgame method in main.js..")

    main_js_path = os.path.join(tmpdir.name, "build/main.js")

    with open(main_js_path, 'r+', encoding="utf-8") as file:
        content = file.read()

        try:
            content = content.replace(
                'return "gamestarter.exe"', 
                'return "gta_sa.exe"'
            )
            content = content.replace(
                r'`"${i}\\${a}" ${c} -a ${t} -p ${n} -g arizona `',
                r'`"${i}\\${a}" -c ${c}  -h ${t} -p ${n} -arizona -mem 2048 -x`'
            )
            
            file.seek(0)
            file.write(content)
            file.truncate()

            logger.info("Successfully change start game method in main.js")
        except:
            logger.error("Failed change start game method in main.js",
                         exc_info=True)
            sys.exit()

