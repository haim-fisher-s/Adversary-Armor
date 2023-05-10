"""logging config for the project."""
import logging
import os


# Delete log file before each run
if os.path.exists('log.txt'):
    os.remove('log.txt')

# Create a root logger
logger = logging.getLogger()

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('log.txt')

# Create a formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Set the formatter on the handler
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log a message
logger.debug('logger is set.')
