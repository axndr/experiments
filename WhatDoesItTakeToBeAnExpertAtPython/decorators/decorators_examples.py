# decorators.py

from time import timeit, sleep


def times(n):
    def wrapper(func):
        def f(*args, **kwargs):
            print('Function Name: {.__name__}'.format(func))
            for _ in range(1, n):
                rv = func(*args, **kwargs)
                print(rv)
            return rv
        return f
    return wrapper


@times(2)
def add(x, y=10):
    return x + y

@times(6)
def mult_by_10(x):
    return 10*x

def arguments(prefix='***'):
    def debug(func):
        def wrapper(*args, **kwargs):
            print(f'{prefix} debugging')
            rv = func(*args, **kwargs)
            return rv
        return wrapper
    return debug


@arguments('--->')
def debug_info(name, age):
    print(f'{name} is {age} years old.')

def timer(func):
    def wrapper(*args, **kwargs):
        start = timeit()
        rv = func(*args, **kwargs)
        end = timeit()
        print(start - end)
        return rv
    return wrapper


@timer
def print1():
    print('test')
    sleep(.5)
    return


@timer
def print2():
    print('test')
    sleep(1)
    return

