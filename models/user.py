#!/usr/bin/python3
"""user class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email: the user email.
        password: password of the user.
        first_name: first name of the user.
        last_name: last name of the user."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
