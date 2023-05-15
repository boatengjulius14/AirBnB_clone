#!/bin/usr/python3
"""Defines User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines User, a subclass of BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
