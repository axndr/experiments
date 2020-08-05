# generators_example.py

from time import sleep


def add_generators(x, y):
    def add(x, y):
        return x + y
    return add


def compute_long():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv


data_set = [10, 0, 3, 54, 2, 34]
def compute():
    for i in range(10):
        sleep(.5)
        yield


def f(x):
    for i in x:
        yield i


def access():
    for i in data_set:
        yield i


set_a = [1, 3, 5, 7, 9]
set_b = [2, 4, 6, 8, 10]
def get_num():
    for x, y in zip(set_a, set_b):
        yield x
        yield


def s1():
    return 10

def s2(x):
    return x * 5

def s3(x):
    return x - 3

def api():
    a = s1()
    yield a
    a = s2(a)
    yield a
    a = s3(a)
    yield a

