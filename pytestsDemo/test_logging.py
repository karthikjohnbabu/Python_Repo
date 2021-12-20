import logging

logger =logging.getLogger(__name__)
fileHandler=logging.FileHandler('logfile.log')
formatter= logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.debug("A debug statement is executed")
logger.info("Information statement")
logger.warning("Once the automation script finds a nagative value in bank account warning will be generated")
logger.error("A Major error has happened")
logger.critical("Critical issue")

