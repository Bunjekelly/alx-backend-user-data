#!/usr/bin/env python3

"""authntification module"""


def _hash_password(self, password: str) -> bytes:
    """Hash a password with bcrypt"""
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())

