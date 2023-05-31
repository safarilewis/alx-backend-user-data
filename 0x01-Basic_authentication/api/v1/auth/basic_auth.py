#!/usr/bin/env python3
"""Basic Auth Class"""
from .auth import Auth


class BasicAuth(Auth):
    """Class containing basic auth methods"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Returns the Base64 part of the Authorization
        header for a Basic Authentication'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(" ")[-1]
        return token
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        '''Returns the decoded value of a 
        Base64 string base64_authorization_header'''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        if not base64_authorization_header.startswith("Basic "):
            return None
        token = base64_authorization_header.split(" ")[-1]
        return token.decode('utf-8')
