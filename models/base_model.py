#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import os
import json
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """
    Attributes and functions for BaseModel class
    """

    if storage_type == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiation of new BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if not hasattr(self, 'updated_at'):
            self.updated_at = self.created_at

    def save(self):
        """Updates attribute updated_at to current time"""
        if storage_type != 'db':
            self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns JSON representation of self"""
        bm_dict = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    bm_dict[key] = value.isoformat()
                else:
                    bm_dict[key] = value
        bm_dict['__class__'] = type(self).__name__
        return bm_dict

    def __is_serializable(self, obj_v):
        """
        Private: checks if object is serializable
        """
        try:
            obj_to_str = json.dumps(obj_v)
            return obj_to_str is not None and isinstance(obj_to_str, str)
        except:
            return False

    def __str__(self):
        """Returns string type representation of object instance"""
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)
