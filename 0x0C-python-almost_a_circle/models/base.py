#!/usr/bin/python3

class Base:
    """
    Base class for managing object creation with unique identifiers.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
        - id (int): Optional. The identifier for the object. If not provided, a new unique identifier will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
