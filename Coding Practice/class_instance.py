class Employee:
   
    def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.email = first + '.' + last + '@company.com'
      self.pay = pay

    #methods are functions that are meant for a class (always takes the first instance as argument)
    def fullname(self):
      return '{} {}'.format(self.first, self.last)

      

emp_1 = Employee('Michael', 'Yoo', '50000')
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

#methods are functions that are meant for a class

#print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname()) # () is for method, without is for attribute
print(Employee.fullname(emp_1))