import logging
import os

# create and configure logger
# python.org has the list of log attributes
from logging import Logger

LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=os.getcwd() + "/pyy.log", level=logging.DEBUG, format=LOG_FORMAT)
logger: Logger = logging.getLogger()

print('done')
logger.info("our first message")
logger.info('second message')

print(logger.level)
