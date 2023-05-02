"""Main module."""
import logging

from advarmor.libs import logging_config  # noqa
from advarmor.libs import tokenizer as TOK


logger = logging.getLogger(__name__)


def hello():
    """Print 'hello module'."""
    print('hello module')  # noqa: T201
    t = TOK.SampleClass()
    logger.debug(t.false())
