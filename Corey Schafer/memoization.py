# https://www.youtube.com/watch?v=a7EjmdQzPqY
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Memoization/sample.py
import time

ef_cache = {}


def expensive_func(num):
    print("Computing {}...".format(num))
    time.sleep(1)
    return num * num


print(expensive_func(4))
print(expensive_func(10))
print(expensive_func(4))
print(expensive_func(10))


# Modified version of expensive_func.
def cheap_func(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}...".format(num))
    time.sleep(1)
    result = num*num
    ef_cache[num] = result
    return result


print(cheap_func(4))
print(cheap_func(10))
print(cheap_func(4))
print(cheap_func(10))
