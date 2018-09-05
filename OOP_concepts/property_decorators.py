# https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/6-property-decorator/oop.py
# Property decorators: Getter, Setter, and Deleter.


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# The first name is different from the others, so the class need to be modified.
# In order to modifying the class without the need for changing the original code which is calling the class,
# one can use a "Property" decorator (also known as "getter" for some other languages, like Java)


class Employee:
    """
    Fixed the issue that other instances will not be updated
    when changing the field "first" after calling the class before-head.
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# In this case, an error occurred, so we still need to modify the class.
# We can use a "Setter" in this case.


class Employee:
    """
    Fixed the issue that other instances will not be updated
    when changing the field "fullname" after calling the class before-head.
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


# As for "Deleter", it is used as an option to delete properties set by users when calling the class.


class Employee:
    """
    Fixed the issue that other instances will not be updated
    when changing the field "fullname" after calling the class before-head.
    """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)
