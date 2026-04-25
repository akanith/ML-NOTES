"""
This script configures the logging system to write log messages to 'app.log'.
It sets the logging level to DEBUG and defines a custom format including timestamp,
logger name, level name, and message.
"""
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', # Fixed asctinme -> asctime
    datefmt='%y-%m-%d %H:%M:%S',
    force=True # Added force=True to override the previous cell's settings
)
