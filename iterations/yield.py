# Generators are iterators, a kind of iterable you can only iterate over once.
# Generators do not store all the values in memory, they generate the values on the fly.


def createiter(num):
    result = list()
    for i in range(num):
        result.append(i*i)
    return result


# A modified generator version of function "createiter".
def creategen(num):
    for i in range(num):
        yield i * i  # "yield" returns a generator.


my_generator = creategen(3)  # The code in the function body does not run.
print(my_generator)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
# print(next(my_generator))  # Error: Stop iterating.

# Alternatively, use for loop to print out all the numbers returned by the generator.
for n in my_generator:
    print(n)
# The first time the "for" calls the generator object created from your function,
# it will run the code in "creategen" from the beginning until it hits yield,
# then it'll return the first value of the loop.
# Then, each other call will run the loop you have written in the function ONE MORE TIME,
# and return the next value, until there is no value to return.
# The generator is considered empty once the function runs but DOES NOT HIT "yield" anymore.


# A even more simpler way to get the same functionality of "creategen" function, is to use a list comprihension.
my_gene = [x*x for x in range(3)]
print(list(my_gene))

my_gene2 = (x*x for x in range(3))  # Recommended, this is a generator version.
print(list(my_gene2))
