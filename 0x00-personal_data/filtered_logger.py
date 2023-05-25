#!/usr/bin/env python3
'''Personal data management'''
from typing import List
import logging
import re


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    '''Returns a log message obfuscated'''
    for item in fields:
        message = re.sub(item+'=.*'+separator, item +
                         '='+redaction+separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Formatting logs'''
        message = super(RedactingFormatter, self).format(record)
        formatted_txt = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)
