#Tutorial 4 - Class inheritance

''' Magic Methods are special methods, sometimes called dunder (with __<>__ format) has special functions

'''
class Employee(): # To define a class the keyword itself is 'class' with classname starting with Captial Letter. For other naming conventions: https://www.python.org/dev/peps/pep-0008/#naming-conventions
    
    raise_amount = 1.04 # This is a class attribute. Its simply defined in the class block.
    
    def __init__(self,fname,lname,pay): #Its a constructor method, invoked whenever an object is created for this class. The keyword 'self' an instance of the class.
        self.fname = fname 
#       object.<somename> = parameter
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'
    
    def __repr__(self): # for developers
        return f'Employee({self.fname},{self.lname},{self.pay})'
    
    def __str__(self): # for users
        return f'{self.fname} {self.lname} - {self.email}'
        
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