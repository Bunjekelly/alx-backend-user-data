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
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        """initialization method that makes
        it accept string fields as arguments"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """the format method to filter values
        in incoming log records using filter_datum"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  super().format(record), self.SEPARATOR)
        return record.msg
