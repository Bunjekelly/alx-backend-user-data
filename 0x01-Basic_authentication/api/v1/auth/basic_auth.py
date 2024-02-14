#!/usr/bin/env python3

""" a module that handles basic authentification of an api"""

from .auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """Class for basic authentication"""
    def __init__(self) -> None:
        """method that initializes the class"""
        super().__init__()
