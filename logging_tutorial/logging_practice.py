# logging_practice.py

import logging
from datetime import datetime


logging.basicConfig(filename='test.log', level=logging.DEBUG)


def decorator(func):
    def wrapper(*args, **kwargs):
        logging.debug(f'{datetime.now()}')
        logging.debug(f'{func.__name__} running. ')
        rv = func(*args, **kwargs)
        logging.debug(f'{func.__name__} returned {rv}.\n')
        return rv
    return wrapper


@decorator
def add(x, y):
    return x + y


@decorator
def mult(x, y):
    return x * y


if __name__ == '__main__':
    a, b = 5, 10
    add(a, b)
    mult(a, b)
