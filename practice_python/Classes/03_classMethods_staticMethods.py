# Class methods take the instance(self) in the class

class Employee:
    
    raise_amt = 1.04 # class variable
    num_of_emps = 0
    
    def __init__(self, first, last, pay): #constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # is day Friday or Sunday worday or not
            return False
        return True

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

emp_1 = Employee('Harry', 'Dadson', 50000)
emp_2 = Employee('Joe', 'Mason', 60000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)