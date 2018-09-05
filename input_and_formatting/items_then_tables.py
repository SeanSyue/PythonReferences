def items_then_tables(a, *args, **kwargs):
    print("------", a, "\n------", sep="", end="")
    for count, thing in enumerate(args):
        print('{}. {}'.format(count, thing), end="; ")  # same as {0}. {1}
    print("\n------", end="")
    for count, thing in enumerate(args):
        print('{1}'.format(count, thing), end="; ")
    print("\n------", end="")
    for name, value in kwargs.items():
        print('{} = {}'.format(name, value), end="; ")  # same as {0} = {1}


items_then_tables('er', "t5t", "fewer", "434", "aaa", a43="43", f3="er")
