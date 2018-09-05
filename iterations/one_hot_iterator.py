from random import randint
import numpy as np


def one_hot_iter(lines, digits=8):
    """
    Output a generator for generating lists of digits in one-hot encoding style.
    Each list is one random row of a numpy eye array.
    :param lines: How many rows.
    :param digits: How many digits in each row.
    :return: A generator.
    """
    eye = np.eye(digits).astype(int)

    def rand_int(lines_):
        for _ in range(lines_):
            yield randint(0, digits-1)

    for i in rand_int(lines):
        yield eye[i]


for n in one_hot_iter(20):
    print(n)
