#!/usr/bin/python3
""" Defines the TestDBStorageDocs and TestDBStorage classes"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Checks the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Intializes the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Checks if models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Checks if tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Checks for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Checks for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Checks for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestFileStorage(unittest.TestCase):
    """Checks the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Checks if all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Checks if all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """Checks if new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """checks if save properly saves objects to file.json"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_get(self):
        """Checks if get properly returns a requested object"""
        user = User(name="User1")
        user.save()
        self.assertEqual(models.storage.get("User", user.id), user)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_count(self):
        """Checks if count properly counts all objects"""
        self.assertEqual(len(models.storage.all()), models.storage.count())