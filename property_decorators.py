#Tutorial 6 - Property Decorators

'''  With Property Decorators methods can be given special functionality. 

'''
class Employee(): # To define a class the keyword itself is 'class' with classname starting with Captial Letter. For other naming conventions: https://www.python.org/dev/peps/pep-0008/#naming-conventions
    
    raise_amount = 1.04 # This is a class attribute. Its simply defined in the class block.
    
    def __init__(self,fname,lname,pay): #Its a constructor method, invoked whenever an object is created for this class. The keyword 'self' an instance of the class.
        self.fname = fname 
#       object.<somename> = parameter
        self.lname = lname
        self.pay = pay
#        self.email = fname + '.' + lname + '@company.com'
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    @fullname.setter
    def fullname(self,name):
        self.fname, self.lname = name.split(' ')
        
    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.lname = None
        
if __name__ == "__main__":
    emp1 = Employee('munavar','hussain',50000) # Creates an object of class employee
    
#    before declaring any property decorator function & before email attribute was commented
#    print(emp1)     #<__main__.Employee object at 0x000001A23FE286D8>
#    print(emp1.email) #munavar.hussain@company.com
#    emp1.fname = 'noorul'
#    print(emp1.email) #munavar.hussain@company.com
    
#    clearly there is no change in email attribute after the fname is assigned a new name. whatif we want the change to be applied while assigning a new value to our attribute.
#    that's why we adapt property decorators. But we do not want other functions or users changing their own code. So we have to provide same experience of using our code as before
#    with additional features
    print(emp1.email)
    emp1.fname = 'noorul'
    print(emp1.email)
#    print(emp1.fullname()) # 'str' object is not callable
    print(emp1.fullname)
    
#    before setter 
#    emp1.fullname = 'ashraf kutbudeen' #can't set attribute
    
    emp1.fullname = 'ashraf kutbudeen'
    
    print(emp1.fullname)
    
    del emp1.fullname
    
    print(emp1.fname)

#Note: the email attribute works as before but with additional feature to dynamically assign value. However remember that it cannot be used as a function with () curly braces.
#    while in our previous examples we defined fullname as a function but it isn't the same here. This example was only given to understand setter and deleter functions.
    