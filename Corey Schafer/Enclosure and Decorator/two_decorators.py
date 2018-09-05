# https://github.com/CoreyMSchafer/code_snippets/blob/master/Decorators/decorators.py
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=2s

# "functools" allows functions use two warp methods without collision.
from functools import wraps
import time


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# Without "functools.wraps", two stacked decorators decorates a function, is equal to
# display_info = my_logger(my_timer(display_info))
# which will lead to a result that we are unexpected
# if
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tom', 22)
