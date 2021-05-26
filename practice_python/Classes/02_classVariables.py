class Employee:

    raise_amount = 1.04 # class variable
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

print(Employee.num_of_emps)

emp_1 = Employee('Harry', 'Dadson', 50000)
emp_2 = Employee('Joe', 'Mason', 60000)

print(Employee.num_of_emps)
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())