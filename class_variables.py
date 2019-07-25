#Tutorial 2 - Class Variables

''' So far we have created variables for instances only (Under __init__ function). Class variables can be understood as a common variable among the instances.
For example, assume there is a need for an attribute where basic pay of an employee has raised to a certain percentage. This raise in pay may be common to all or a set of employees.
In such scenarios class variables come handy.

'''
class Employee(): # To define a class the keyword itself is 'class' with classname starting with Captial Letter. For other naming conventions: https://www.python.org/dev/peps/pep-0008/#naming-conventions
    
    raise_amount = 1.04 # This is a class attribute. Its simply defined in the class block.
    
    def __init__(self,fname,lname,pay): #Its a constructor method, invoked whenever an object is created for this class. The keyword 'self' an instance of the class.
        self.fname = fname 
#       object.<somename> = parameter
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
    
    def fullname(self):
        return f"{self.fname} {self.lname}"
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amount) #self is necessary for class variables


if __name__ == "__main__":
    emp1 = Employee('munavar','hussain',50000) # Creates an object of class employee
    emp2 = Employee('ashraf','kutbudee',60000)
    
    print('Before:')
    print(Employee.raise_amount)
#    print(Employee.__dict__) use __dict__ to see the attributes and methods a class/instance holds. Employee class obviously holds raise amount attribute.
#    print(emp1.__dict__)  {'fname': 'munavar', 'lname': 'hussain', 'pay': 50000, 'email': 'munavar.hussain@company.com'} ^ and its instance do not.

    print(emp1.raise_amount)    
    print(emp2.raise_amount)
    
    emp1.raise_amount = 1.05
    emp2.raise_amount = 1.06
    Employee.raise_amount = 1.07
    
    emp3 = Employee('john','william',70000)
    
    print('After:')
    print(Employee.raise_amount)
    print(emp1.raise_amount)    
    print(emp2.raise_amount)
    print(emp3.raise_amount)
#
#Before:
#1.04
#1.04
#1.04
#After:
#1.07
#1.05
#1.06
#1.07

#    Things to note: each instance has its own copy of raise_amount and any changes are only applied to its copy.