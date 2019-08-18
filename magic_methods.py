#Tutorial 5 - Magic Methods

''' Magic Methods are special methods, sometimes called dunder (with __dunder__ format) has special functions

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
        return f'{self.fname} {self.lname}'
    
    def __repr__(self): # for developers
        return f'Employee({self.fname},{self.lname},{self.pay})'
    
    def __str__(self): # for users
        return f'{self.fname} {self.lname} - {self.email}'
    
    def __add__(self,other): #employee objects
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
if __name__ == "__main__":
    emp1 = Employee('munavar','hussain',50000) # Creates an object of class employee
    emp2 = Employee('ashraf','kutbudeen',60000)
    
#    print(emp1) #without dunders prints <__main__.Employee object at 0x000001831605D908>
    print(emp1) #with _repr__ function only prints Employee(munavar,hussain,50000)
    print(emp1) #with both functions (__repr__,__str__) prints munavar hussain - munavar.hussain@company.com
#    It is understood __str__ has high priority when both functions are declared.
#    However both functions can be induvidually called.
    print(emp1.__repr__())
    print(emp2.__str__())  
#Employee(munavar,hussain,50000)
#ashraf kutbudeen - ashraf.kutbudeen@company.com
    print(emp1 + emp2)  #__add__ dunder similarly there are sub, mul and more @ https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
# that's how integer addition is different from string addition in python. i.e int object and str object have different dunder __add__()
    
    print(len('mh')) #2 the keyword len is also a dunder method. it can be used as
    print('mh'.__len__())
    
#    print(len(emp1)) object of type 'Employee' has no len() 
#                       this shows up when len for employee is not declared
    print(emp1.__len__()) #14