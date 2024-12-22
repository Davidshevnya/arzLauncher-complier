import os
import sys

import app_logger
import asar

logger = app_logger.get_logger(__name__)

def main(path_to_file):
    if os.path.exists(path_to_file) and os.path.isfile(path_to_file):
        logger.info(f"Asar file path: {os.path.realpath(path_to_file)}")
        asar.extract(os.path.realpath(path_to_file))

        launcher_type = int(input("""Which launcher will we change?
                                  \n[1] Korista
                                  \n[2] Suvorov
                                    \n[3] Original
                                  \nYour answer:"""))
        
        asar.change_links_in_files(launcher_type)

        if launcher_type == 2:
            asar.change_start_game_method()

        asar.pack()
        logger.info(
            """You have successfully packaged app.asar. There is only\
            \none step left: copy it from the output directory and move\
            \nit to the resources folder with the launcher"""
        )
    else:
        logger.error(f"Asar file was not found.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python main.py <path_to_app_asar>")
    else:
        main(sys.argv[1])
        

