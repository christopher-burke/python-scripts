#!/usr/bin/env python3

"""Basic Logging template."""

import logging

LOG_FORMAT_STRING = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename='log.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT_STRING,
                    filemode='a')

logger = logging.getLogger(name=None)

msg = 'This is a {} message.'

logger.debug(msg.format(logger.debug.__name__))
logger.info(msg.format(logger.info.__name__))
logger.warning(msg.format(logger.warning.__name__))
logger.error(msg.format(logger.error.__name__))
logger.critical(msg.format(logger.critical.__name__))
