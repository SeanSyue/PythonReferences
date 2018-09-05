# https://youtu.be/rq8cL2XMM5M
# Class methods can be seen as additional constructors.


class Employee:
    """
    Class object of employee information.
    """

    # Class variable:
    raise_amt = 1.05

    # Instance variable (or static variable) :
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def get_fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str_):
        first_, last_, pay_ = emp_str_.split('-')
        return cls(first_, last_, pay_)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


# Using a class method to change class variable(s).
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# When one need to parse hyphen-separated string to fit the class.
emp_str = 'John-Doe-70000'
first, last, pay = emp_str.split('-')
new_emp= Employee(first, last, pay)

# To simply the process, one can use a class method to do so instead.
new_emp = Employee.from_string(emp_str)
