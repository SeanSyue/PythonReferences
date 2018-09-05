# https://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/
# There are five levels of logging (in ascending order): DEBUG, INFO, WARNING, ERROR and CRITICAL.

import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="basic sample.log", level=logging.DEBUG)

logging.debug("Main debug message")
logging.info("Main informational message")
logging.error("Main error message!")
