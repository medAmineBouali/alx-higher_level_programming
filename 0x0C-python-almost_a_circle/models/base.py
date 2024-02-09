#!/usr/bin/python3

class Base:
    __nb_objects = 0
    def __init__(self, id = None):
        if not (id is None):
            self.id = id
        else:
            self.new_obj()
            self.id = self.__nb_objects
    @classmethod
    def new_obj(cls):
        cls.__nb_objects += 1