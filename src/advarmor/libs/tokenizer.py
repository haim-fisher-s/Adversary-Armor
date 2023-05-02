"""
Module responsible to creates tokens based on model parameters.

Contains:
    - Tokenizer
"""
import logging

from . import logging_config  # noqa


logger = logging.getLogger(__name__)


class Tokenizer:
    """Class to generate the tokens."""

    def __init__(self):
        """Initiatlizes Tokenizer class."""
        return

    @classmethod
    def generate_tokens(self):
        """Generate tokens based on model parameters."""
        logger.debug('generate_tokens started')
