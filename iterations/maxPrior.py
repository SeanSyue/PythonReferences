# https://zhuanlan.zhihu.com/p/33593039

# finding the max prior to the current item
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
results = []
current_max = 0
for i in a:
    current_max = max(i, current_max)
    results.append(current_max)

print(results)  # results = [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]


# ============================================================
# Modified:
# ============================================================
def max_generator(numbers):
    current_max = 0
    for i in numbers:
        current_max = max(i, current_max)
        yield current_max


a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
results = list(max_generator(a))
print(results)


# ============================================================
# Modified:
# ============================================================
from itertools import accumulate
a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
resutls = list(accumulate(a, max))
print(results)
