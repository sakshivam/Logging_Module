import logging
import logging.config
import yaml

with open('config.yaml', 'r') as f:

    # log_config = yaml.safe_load(f.read())
    log_config = yaml.load(f, Loader=yaml.FullLoader)

logging.config.dictConfig(log_config)

logger = logging.getLogger('dev')
# logger.setLevel(logging.INFO)

logger.debug("debugging something")
logger.info("some message")
logger.warning("Warning, the program may not function properly")
logger.error("something went wrong")
logger.critical("The program crashed")