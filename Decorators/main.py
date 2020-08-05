from functools import wraps, partial


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Executed Before {original_function.__name__}')
        result = original_function(*args, **kwargs)
        print(f'Executed After {original_function.__name__}\n')
        return result
    return wrapper_function


def kwarg_decorator(user="default"):
    def debug(func):
        def wrapper(*args, **kwargs):
            print(user)
            return func(*args, **kwargs)
        return wrapper
    return debug


def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{prefix} {func.__qualname__} ', end='')
        return func(*args, **kwargs)
    return wrapper


@debug
def display_info(name, age):
    print(f'display_info ran with arguments {name} and {age}')


@debug(prefix='10-1-1993 >>> ')
def user_info(user):
    print(f'user_info was ran by {user}')


# def time_of_day_greeting(say_hello):
#     def wrapper_function(*args, **kwargs):
#         print(f'A fine {kwargs} we\'re having, isn\'t it?')
#         say_hello(*args, **kwargs)
#         print('Hope you have a swell time!')
#
#
# @time_of_day_greeting
# def say_hello(name):
#     print(f'Hello, {name}')


if __name__ == '__main__':
    display_info('John', 25)
    user_info('Sarah')
