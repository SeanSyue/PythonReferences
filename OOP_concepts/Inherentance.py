# https://www.youtube.com/watch?v=rq8cL2XMM5M


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Hr(Employee):
    pass


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


hr_1 = Hr('Sean', 'Syue', 50000)
print(hr_1.email)


# -------------- Useful functions --------------
# To look up the chain of inheritance(a.k.a. the "method resolution order") and other information of a class,
# one can use the built-in help() method.
print(help(Developer))

# To judge whether an instance is belong to a certain class, one can use the built-in isinstance() method:
print(isinstance(hr_1, Hr))  # Undoubtfully it return true.
print(isinstance(hr_1, Employee))  # This one also returns true.

# To judge whether an instance is belong to a subclass of a certain class, one can use the built-in isinstance() method:
print(issubclass(Hr, Employee))  # Undoubtfully it return true.


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()