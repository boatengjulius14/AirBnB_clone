#!/usr/bin/python3
"""Defines the city module"""
from models.base_model import BaseModel


class City(BaseModel):
    """Definition of City class, subclass of BaseModel"""

    state_id = ""
    name = ""
