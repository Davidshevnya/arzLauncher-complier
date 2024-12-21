import tempfile
import os

import app_logger

logger = app_logger.get_logger(__name__)

def setup_tmpdir():
    try:
        tmpdir = tempfile.TemporaryDirectory()
        tmpdir.name += "/output"
    except:
        logger.error("Failed to create temporary folder")
    
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
    else:
        os.makedirs(output_dir)
        logger.info("Output directory successfully created")
