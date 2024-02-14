#!/usr/bin/env python3

""" a module that handles basic authentification of an api"""

from .auth import Auth
from typing import TypeVar
import base64


class BasicAuth(Auth):
    """Class for basic authentication"""
    def __init__(self) -> None:
        """method that initializes the class"""
        super().__init__()

    @staticmethod
    def extract_base64_authorization_header(authorization_header: str) -> str:
        """a method that returns the Base64 part of the
        Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        base64_auth = authorization_header.split('Basic ')[1]
        return base64_auth

    @staticmethod
    def decode_base64_authorization_header(
            base64_authorization_header: str) -> str:
        """that returns the decoded value of a
        Base64 string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    @staticmethod
    def extract_user_credentials(
            decoded_base64_authorization_header: str) -> (str, str):
        """method that  returns the user email
        and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':')
        return email, password
