import numpy as np

arr = np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])]
arr2 = np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])]

print(arr)
print(arr2)
