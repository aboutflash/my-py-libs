import json
import locale
from locale import currency, LC_MONETARY

from aio_rsiapi.__about__ import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __summary__,
    __title__,
    __uri__,
    __version__,
)

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
    "to_json",
    "cents_to_dollar_format",
]


def to_json(data) -> dict:
    try:
        decoded = data.decode('utf-8')
        return json.loads(decoded)
    except UnicodeDecodeError:
        return json.loads('')


def cents_to_dollar_format(cents) -> str:
    locale.setlocale(category=LC_MONETARY, locale='en-US')
    return currency(cents * 0.01, True, True, False)
