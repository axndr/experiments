# timer_practice.py

from time import time


def timer_context(number=1000):
    def manager(func):   
        def wrapper(*args, **kwargs):
            start = time()
            for _ in range(number):
                rv = func(*args, **kwargs)
                print(f'{_}: {rv}')
            end = time()
            print(f'{end - start:f} sec(s)')
            return rv
        return wrapper
    return manager


@timer_context(80)
def add(x, y):
    return x + y

