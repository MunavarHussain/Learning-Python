#Tutorial 4 - Class inheritance

''' Class inheritance is about a subclass inheriting the attributes and methods of a parent class. Such methods can be overwritten and have completely new functionality.

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
 

class Developer(Employee): #subclass developer inherits class Employee 
    raise_amount = 1.03
    def __init__(self,fname,lname,pay,prog_lang):
        super().__init__(fname,lname,pay)
#        Employee.__init__(self,fname,lname,pay)
        self.prog_lang = prog_lang
    
class Manager(Employee):
    raise_amount = 1.05
    
    def __init__(self,fname,lname,pay,employees=None):
        super().__init__(fname,lname,pay)
        if(employees == None):
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        self.employees.append(emp)
    
    def remove_emp(self,emp):
        self.employees.remove(emp)
        
if __name__ == "__main__":
    dev1 = Developer('munavar','hussain',50000,'python') # Creates an object of class employee
    dev2 = Developer('ashraf','kutbudeen',60000,'java')
    
    mng1 = Manager('corey','schafer',70000,[dev1])
    
    print(mng1.email)
    mng1.add_emp(dev2)
    print(mng1.employees)
    mng1.remove_emp(dev2)
    print(mng1.employees)
    
    print(isinstance(mng1,Employee))
    
#    corey.schafer@company.com
#[<__main__.Developer object at 0x0000019ACF023470>, <__main__.Developer object at 0x0000019ACF023668>]
#[<__main__.Developer object at 0x0000019ACF023470>]
#True
    