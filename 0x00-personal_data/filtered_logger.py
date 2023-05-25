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
