import numpy as np
arr1 = np.random.permutation(10)
arr2 = np.random.permutation([1, 4, 9, 12, 15])

arr = np.arange(9).reshape((3, 3))
arr3 = np.random.permutation(arr)

print(arr1)
print(arr2)
print(arr3)
