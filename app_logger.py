import logging

def get_file_handler():
    log_format = f"[%(asctime)s]  [%(levelname)s]  %(message)s"
    file_handler = logging.FileHandler("compilier_log.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler

def get_stream_handler():
    _log_format = f"%(asctime)s.%(msecs)03d > %(message)s"
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format,
                                                  datefmt="%H:%M:%S"))
    return stream_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger

