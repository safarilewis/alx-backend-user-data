#!/usr/bin/env python3
'''Authorization class'''
from flask import request
from typing import List, TypeVar


class Auth:
    '''Class containing all auth methods'''

    def require_auth(self, path: str, excluded_paths: List[str], strict_slashes=False) -> bool:
        """Checks if the path provided requires authentication """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        for paths in excluded_paths:
            if path == paths:
                return False
            return True

    def authorization_header(self, request=None) -> str:
        """Performs request validation to secure the API"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns Flask request object None-request"""
        return request
