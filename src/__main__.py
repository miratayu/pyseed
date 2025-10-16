import logging

import sandbox

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("hello")
    sandbox.call_hello('Python')
    num = sandbox.increment(-1)
    logger.info(f"{num=}")
    num = sandbox.increment(100)
    logger.info(f"{num=}")
