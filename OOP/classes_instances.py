#Tutorial 1 - Understanding classes and instances

'''Object oriented programming is a way of programming, that in its unique way allows us to group data based on objects.It is indeed inspired from real world.

In tutorial 1 we'll learn about class and instances.
Classes are blueprint associated with some data and functions. In OOP we call those attributes(variables) and methonds respectively.
Whereas Instances are a copy of a class that inherit attributes & methods of that class and also has its own attributes and methods.
Let's create a employee class to understand the concept.

'''
class Employee(): # To define a class the keyword itself is 'class' with classname starting with Captial Letter. For other naming conventions: https://www.python.org/dev/peps/pep-0008/#naming-conventions
    def __init__(self,fname,lname,pay): #Its a constructor method, invoked whenever an object is created for this class. The keyword 'self' an instance of the class.
        self.fname = fname 
#       object.<somename> = parameter
        self.lname = lname
        self.pay = pay
    def fullname(self):
        return f"{self.fname} {self.lname}"

if __name__ == "__main__":
    emp1 = Employee('munavar','hussain',50000) # Creates an object of class employee
    emp2 = Employee('ashraf','kutbudee',60000)
    
    print(emp1.fname)
    print(emp2.fname)
    print(emp1.fullname())
    
#munavar
#ashraf
#munavar hussain
    
#    Attributes and methods created so far are for instances not for the class. Hence,
#    print(Employee.fname) throws error.