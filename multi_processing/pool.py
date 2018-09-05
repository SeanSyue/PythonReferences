"""https://docs.python.org/3.6/library/multiprocessing.html"""
from multiprocessing import Pool


def f(x):
    return x*x


with Pool(5) as p:
    print(p.map(f, [1, 2, 3]))