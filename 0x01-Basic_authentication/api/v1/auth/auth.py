#!/usr/bin/env python3
'''Authorization class'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''Class that will contain auth methods'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns false-path """
        return path

    def authorization_header(self, request=None) -> str:
        """Returns None, flast request object"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns Flask request object None-request"""
        return request
