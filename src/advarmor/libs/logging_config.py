"""logging config for the project."""
import logging


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
