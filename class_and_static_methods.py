#Tutorial 3 - Class and static methods

''' We'll see examples for a class and a static method.

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

    @classmethod # Special keyword to define a class method
    def set_raise_amount(cls, pay):
        cls.raise_amount = pay
        
    @classmethod
    def format_str(cls,txt):
        fname, lname, pay = txt.split('-')
        return Employee(fname,lname,int(pay))
    
#    note in a static function, no class or instance is called.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # .weekday() return 0-6 representing monday-sunday
            return False
        return True
        
if __name__ == "__main__":
    emp1 = Employee('munavar','hussain',50000) # Creates an object of class employee
    emp2 = Employee('ashraf','kutbudeen',60000)
    Employee.set_raise_amount(1.05)
    print(Employee.raise_amount)
    print(emp1.raise_amount)
#    let's take a situation where the client has a xl sheet of data formatted as fname-lname-pay. Rather than hard coding, it is easy to call a function which formats the xl text.
    emp3 = Employee.format_str('john-william-70000')
    print(emp3.fname)
    print(emp3.lname)
    print(emp3.email)
    print(emp3.pay)
    
    import datetime
    day = datetime.date(2019, 7, 26)
    
    print(Employee.is_workday(day))

#1.05
#1.05
#john
#william
#john.william@company.com
#70000
#True