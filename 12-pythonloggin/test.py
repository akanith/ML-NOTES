"""
This script demonstrates the use of the logging configuration from log.py.
It defines an add function that logs its operations and performs some sample logging.
"""
from log import logging

def add(a, b):
    logging.info("Adding %s and %s", a, b)
    return a + b

logging.debug("debug message")
add(10, 20)
logging.warning("warning message")