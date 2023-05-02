"""Main module."""
import datetime
import logging

from advarmor.libs import logging_config  # noqa
from advarmor.libs.tokenizer import Tokenizer


logger = logging.getLogger(__name__)


def main():
    """Run app flow."""
    start_time = datetime.datetime.now()
    
    t = Tokenizer()
    t.generate_tokens()

    end_time = datetime.datetime.now()
    logger.debug(f'advarmor done in :{end_time - start_time}')


if __name__ == "__main__":
    main()
