# https://zhuanlan.zhihu.com/p/33593039

# Syntax of list comprehension(列表解析）: 
# result = [do_something_with(item) for item in item_list]
# Same way to get a generator:
# result = (do_something_with(item) for item in item_list)


# ============================================================
# Modifying a long for-loop expression
# ============================================================
# results = []
# for item in item_list:
# # setups
# # condition
# # processing
# # calculation
# results.append(result)

# -*- Can be replaced by: -*-

# def process_item(item):
# # setups
# # condition
# # processing
# # calculation
# return result
#
# results = [process_item(item) for item in item_list]

# ============================================================
# Modifying a nested for-loop expression
# ============================================================

# results = []
# for i in range(10):
#   for j in range(i):
#   results.append((i, j))

# -*- Can be replaced by: -*-

# results = [(i, j)
#  for i in range(10)
#   for j in range(i)]

