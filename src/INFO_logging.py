import logging

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level

logger = logging.getLogger("test_info")
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler(filename='test_info.log')
logFileFormatter = logging.Formatter(
    fmt=f"%(levelname)s %(asctime)s \t L%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler.setFormatter(logFileFormatter)
#set filter to log only INFO lines
fileHandler.addFilter(MyFilter(logging.INFO))
logger.addHandler(fileHandler)

# write an INFO messages from logs to log file
logger.debug("debugging something")
logger.info("some message")
logger.warning("Warning, the program may not function properly")
logger.error("something went wrong")
logger.critical("The program crashed")