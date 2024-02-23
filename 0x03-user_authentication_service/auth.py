#!/usr/bin/env python3

"""authntification module"""

from db import DB
import bcrypt
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from user import User
from Typing import Union


def _hash_password(self, password: str) -> bytes:
    """Hash a password with bcrypt"""
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a uuid and return its string representation"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user and return a user object"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user's login credentials and return True if
        they are correct or False if they are not"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_password = user.hashed_password
        passwd = password.encode("utf-8")
        return bcrypt.checkpw(passwd, user_password)

    def create_session(self, email: str) -> Union[None, str]:
        """ Create a session_id for an existing user and update the user's
        session_id attribute """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Takes a session_id and returns the corresponding user,
        if one exists, else returns None"""
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """Take a user_id and destroy that user's session and update their
        session_id attribute to None"""
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset_token uuid for a
        user identified by the given email"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Updates a user's password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError()

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password, reset_token=None)
