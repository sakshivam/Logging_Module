import logging
import sys

logger = logging.getLogger("test")
# assert logger.level == logging.NOTSET # new logger has NOTSET level
# assert logger.getEffectiveLevel() == logging.WARN # and its effective level is the root logger level, i.e. WARN
logger.setLevel(level=logging.INFO)

logStreamFormatter = logging.Formatter(
  fmt=f"%(levelname)-8s %(asctime)s \t %(filename)s @function %(funcName)s line %(lineno)s - %(message)s",
  datefmt="%H:%M:%S"
)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(logStreamFormatter)
consoleHandler.setLevel(level=logging.ERROR)

logger.addHandler(consoleHandler)

logger.debug("debugging something")
logger.info("some message")
logger.warning("Warning, the program may not function properly")
logger.error("something went wrong")
logger.critical("The program crashed")