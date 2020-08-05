# itertools practice - iter.py

import itertools


class MyCounter:
    def __init__(self, start=0, end=99):
        self.start = start
        self.end = end
        self.value = start
   
    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.value += 1
            yield self.value

    def __repr__(self):
        return f'{self.value}'



class bCounter:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            yield self.number 
            self.number += 1

