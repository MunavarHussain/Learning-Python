'''
int('10')     - returns integer value 10
int('10+10')  - returns value error 
eval('10+10') - returns integer 20
'''

'''
Any number of arguments in a function can have a default value. 
But once we have a default argument, all the arguments to its right must also have default values.

def greet(msg = "Good morning!", name):
	...
Above function generates error "SyntaxError: non-default argument follows default argument"
while the below one is acceptable.
def greet(name,msg = "Good morning!"):
	...
'''

'''
Sometimes, we do not know in advance the number of arguments that will be passed into a function.
Python allows us to handle this kind of situation through function calls with arbitrary number of arguments.
In the function definition we use an asterisk (*) before the parameter name to denote this kind of argument.
'''
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")

'''
Modifying Global variables
'''
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)