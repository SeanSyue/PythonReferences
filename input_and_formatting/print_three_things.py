def print_three_things(a, b, c):
    print('a = {1}, b = {0}, c = {1}， d = {2}'.format(a, b, c))


my_list = ['aardvark', 'baboon', 'cat']
print_three_things(*my_list)
