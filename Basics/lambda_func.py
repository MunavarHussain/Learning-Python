'''
A lambda function is a small anonymous function. That means it is a function but without a name.
lambda arguments : expression
'''
x = lambda a : a + 10
print(x(5)) # 15

x = lambda a, b : a * b
print(x(5, 6))  #30
'''
when to use?
Say, we have two functions doubler() & tripler() in our program.
def doubler(n):                            def tripler(n):
    return n*2                                  return n*3
what if we need a quadripler? We would have to add another function.
We could use lamba function here.
'''
def lda_mul(n):
    return lambda a : a*n

print(lda_mul(5)(2)) #10
'''
Though the mentioned example suffices its purpose. It may not be an appealing use case.
Generally, lambda function is used with other functions such as map, filter. Let's take a look at both.
The filter fucntion takes two parameter a funtion and a list. filter() returns a new list whose elements are from the original list which returned true in the original function.
let's see an example to filter numbers divisible by 6 from list.
'''
list1 = list(range(25))

print(list(filter(lambda p: (p%6==0) , list1))) #[0, 6, 12, 18, 24]

'''
similarly map() returns a new list whose elements are operated with functions passed.
let's see an example to square elements from list.
'''
print(list(map(lambda m: m**2, list1 )))

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576]
