import logging.config


def getLogger(level: str):
    logging.config.fileConfig('logging_config.ini')

    if level == "info":
        logger = logging.getLogger('InfoLogger')
        return logger

    elif level == "warn":
        logger = logging.getLogger('WarnLogger')
        return logger

    elif level == "error":
        logger = logging.getLogger('ErrorLogger')
        return logger
