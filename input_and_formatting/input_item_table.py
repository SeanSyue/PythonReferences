def items_then_tables(*args):
    print("\n------", end="")
    for count, thing in enumerate(args):
        print('{1}'.format(count, thing), end="; ")
    print("\n------", end="")
    for count in enumerate(args):
        print('{1}'.format(count, thing), end="; ")
    print("\n------", end="")
    for thing in enumerate(args):
        print('{1}'.format(count, thing), end="; ")


a = ['er', "t5t", "fewer", "434", "aaa"]
print(list(enumerate(a)))
items_then_tables('er', "t5t", "fewer", "434", "aaa")
