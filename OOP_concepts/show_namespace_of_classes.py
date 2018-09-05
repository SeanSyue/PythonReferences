# https://github.com/CoreyMSchafer/code_snippets/blob/master/Object-Oriented/2-Class-Instance-Variables/oop.py


class Employee:
    """
    Class object of employee information.
    """

    # Class variable:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def get_fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# Use "__dict__" to get the namespaces of a class:
emp = Employee('Corey', 'Schafer', 50000)
print(emp.__dict__)  # Instance "emp" has no property of "raise_amount".
print(Employee.__dict__)

emp.raise_amount = 1.04
print(emp.__dict__)  # Now instance "emp" has the property of "raise_amount".
