#!/usr/bin/env python3
'''Encrypting user's passwords'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Returns a salted hash password'''
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Checks if password was hashed correctly'''
    check = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return check
