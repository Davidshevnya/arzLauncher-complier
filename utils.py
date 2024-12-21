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