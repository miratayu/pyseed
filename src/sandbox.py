import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def call_hello(text: str = 'World') -> None:
    logger.info(f"Hello {text}!!")


def increment(num: int = 0) -> int:
    num += 1
    return num
