#!/usr/bin/python3
"""user module"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class."""

    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)