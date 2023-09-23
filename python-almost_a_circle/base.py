
"""This module creates the class name is a base class"""

class Base:
    """this is a base class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function to init id to istance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            