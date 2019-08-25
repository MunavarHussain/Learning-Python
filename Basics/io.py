'''
print() and input() are basic stdio write and read functions respectively.
let's see some examples to understand both functions, its usage and capabilities.
'''
print('hello world')

var = 10 # var is not a keyword in python

print('The value of variable var is',var)

'''
Output:
hello world
The value of variable var is 10
'''

'''
Note that a new line forms inbetween both print()s and a space is created after 'is' in second print statement by default.
all parameters of a print() function is
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''

print('No new line',end='')
print('No separator',var,sep='',flush=True)
'''No new lineNo separator10'''
''' The file parameter is the object where the values are printed and its default value is sys.stdout. flush doesnt has no common use case.'''

print('print var < {} > here'.format(var))
'''print var < 10 > here
same can be acheived by
'''
print(f'print var < {var} > here')
print('print var < %d > here' %var)
