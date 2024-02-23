#!/usr/bin/env python3

"""authntification module"""


def _hash_password(self, password: str) -> bytes:
    """Hash a password with bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
