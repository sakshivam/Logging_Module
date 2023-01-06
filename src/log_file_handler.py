import logging

logger = logging.getLogger("test")
assert logger.level == logging.NOTSET # new logger has NOTSET level
assert logger.getEffectiveLevel() == logging.WARN # and its effective level is the root logger level, i.e. WARN
# logger.setLevel(level=logging.INFO)

logFileFormatter = logging.Formatter(
    fmt=f"%(levelname)s %(asctime)s \t L%(lineno)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = logging.FileHandler(filename='test.log')
fileHandler.setFormatter(logFileFormatter)

fileHandler.setLevel(level=logging.INFO)
logger.addHandler(fileHandler)


logger.debug("debugging something")
logger.info("some message")
logger.warning("Warning, the program may not function properly")
logger.error("something went wrong")
logger.critical("The program crashed")