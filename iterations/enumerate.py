seasons = ['Spring', 'Summer', 'Fall', 'Winter']
enum = enumerate(seasons)
print(enum)
print(type(enum))
print(list(enum))

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
