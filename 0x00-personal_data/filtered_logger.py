#!/usr/bin/env python3
'''Personal data management'''
from typing import List
import logging
import re
import mysql.connector
import os
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    '''Returns a logging.Logger object'''
    logger = logging.getLogger("user_data")
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connctor.connections.MySQLConnections:
    '''Creates connection to db'''
    host = os.getenv(PERSONAL_DATA_DB_HOST)
    name = os.getenv(PERSONAL_DATA_DB_NAME)
    user = os.getenv(PERSONAL_DATA_DB_USERNAME, "root")
    password = os.getenv(PERSONAL_DATA_DB_PASSWORD, "")
    conn = mysql.connector.connect(
        user=user, password=password, host=host, database=name)
    return conn


def main():
    '''Logs info about user in a table'''
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    for row in cursor:
        message = "".join("{}={}; ".format(k, v) for k, v in zip(fields, row))
        logger.info(message.strip())
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
