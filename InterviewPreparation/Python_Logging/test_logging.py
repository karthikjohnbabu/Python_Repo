import logging
def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # for addHandler pass the fileHandler.
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info(" Information statement")
    logger.warning("Something is in warning Mode")
    logger.error("A major error has occured")
    logger.critical(" Critical issue")
