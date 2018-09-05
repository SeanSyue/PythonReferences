"""https://docs.python.org/3.6/library/multiprocessing.html"""
from multiprocessing import Process


def f(name):
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
