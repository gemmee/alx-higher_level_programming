#!/usr/bin/python3
"""
    This is a 11-student module
"""


class Student:
    """A class that defines a student.
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for _ in attrs:
                if type(_) is not str:
                    return obj

            d_obj = {}
            for i in range(len(attrs)):
                for key in obj:
                    if attrs[i] == key:
                        d_obj[key] = obj[key]
                        break
            return d_obj
        return obj

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        """
        for key in json:
            self.__dict__[key] = json[key]
