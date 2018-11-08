#!/usr/bin/env python3

"""logging example."""


import logging

debug = False  # Possible verbose command line argument.

logging.basicConfig(level=logging.WARNING,
                    format="%(msg)s")
if debug:
    logging.getLogger().setLevel(logging.DEBUG)


LOG = logging.getLogger('demo')

LOG.debug("Program did a thing.")
LOG.info("Program is telling you something important.")
LOG.warning("Something happened, you should be aware of it.")
