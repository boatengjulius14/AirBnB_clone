#!/usr/bin/python3
"""Defines the review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of Review class, subclass of BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
