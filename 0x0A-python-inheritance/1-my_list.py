#!/usr/bin/python3
"""A parent class that inherits child class"""
list = []
class MyList(list):
    def __init__(self, list):
        self.list = list

    def print_sorted(self, list):
        self.list = self.list.sort()
        return self.list
