# https://www.youtube.com/watch?v=BJ-VvGyQxho
import datetime


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

    # Since judging whether is a workday or not simply influence by date itself,
    # which means it has no relation with class or instances of class.
    # So method "is_workday(day)" can be set as static methond
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


my_date = datetime.date(2018, 2, 12)
print(Employee.is_workday(my_date))
