#!/usr/bin/python3
"""
    This is a 9-student module
"""


class Student:
    """A class that defines a student by

    three public instance attributes and
    one public method to_json()
    """
    def __init__(self, first_name, last_name, age):
        """Instantiates the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of Student instance
        """
        return self.__dict__.copy()
