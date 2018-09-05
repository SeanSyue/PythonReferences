# https://www.youtube.com/watch?v=BJ-VvGyQxho


class Employee:
    """
    Class object of employee information.
    """

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


print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(Employee.num_of_emps)
