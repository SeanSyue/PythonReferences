class DecoratorClass(object):

    def __init__(self, original_func):
        self.original_func = original_func

    # Use __call__ method to mimic the wrapper function.
    def __call__(self, *args, **kwargs):
        print(f"Call method executed this before {self.original_func.__name__}.")
        return self.original_func(*args, **kwargs)


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f"Wrapper executed this before {original_func.__name__}.")
        return original_func(*args, **kwargs)
    return wrapper_func


@DecoratorClass
def display_by_cls(name, age):
    print(f"display_by_cls ran with arguments ({name}, {age}).")


@decorator_func
def display_by_func(name, age):
    print(f"display_by_func ran with arguments ({name}, {age}).")


display_by_func('John', 25)
display_by_cls('John', 25)
