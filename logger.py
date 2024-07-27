from loguru import logger

def setup_logger():
    logger.add("sqlguard.log", rotation="10 MB")
