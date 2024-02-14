#!/usr/bin/env python3

""" a module that handles basic authentification of an api"""

from .auth import Auth
from typing import TypeVar


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
