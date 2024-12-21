from asarPy import pack_asar, extract_asar

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
        
        
        

            
            
