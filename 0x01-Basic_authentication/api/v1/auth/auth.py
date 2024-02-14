#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """a class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """returns None - request will be the Flask request object"""
        return None
