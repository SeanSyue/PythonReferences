my_list = [x*x for x in range(3)]
for i in my_list:
    print(i)
print("my_list:", my_list)

my_generator = (x*x for x in range(3))
for i in my_generator:
    print(i)
print("my_generator:", my_generator)
print("type:", type(my_generator))

# One can use:
# print(list(my_generator))
# But converting to list will lose the benefit of generators.
