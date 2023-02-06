#!/usr/bin/python3
"""A parent class that inherits child class"""
class MyList:
    def __init__(self, list):
        self.list = list

    def print_sorted(self):
        self.list.sort()
        return self.list
