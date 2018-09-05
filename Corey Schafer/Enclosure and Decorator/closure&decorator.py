# https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Closures/closure.py
# https://www.youtube.com/watch?v=swU3c34d2NQ&t=11s

# Closures and decorator.
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


add_logger = logger(add)
add_logger(3, 3)


# Alternatively, one can use "decorator" to make the code simpler and easier to understand.
@logger
def log_add(x, y):
    return x + y


log_add(2, 3)
