#!/usr/bin/env python3

""" a function called filter_datum that returns the log message obfuscated"""

import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """a function called filter_datum that returns
    the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}[^{separator}]*",
                         f"{field}{redaction}", message)
    return message