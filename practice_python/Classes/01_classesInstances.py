# class is blueprint for creating instancess ex. Employee()
# instances uses class emp_1 = Employee(), emp_2 = Employee()

class Employee:

    def __init__(self, first, last, pay): #constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('Harry', 'Dadson', 50000)
emp_2 = Employee('Joe', 'Mason', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())