#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Bosco"):
        self.name = name


    def get_name(self):
        return self._name

    def set_name(self, name):
        if(type(name) in (str)):
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
