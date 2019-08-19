import numpy as np

data = [[1,2,3],[4,5,6]]
    # list of lists format
print(type(data))
"""
<class 'list'>
"""
data = np.array(data)
print(data)
"""
[[1 2 3]
 [4 5 6]]
"""
print(type(data))
"""
<class 'numpy.ndarray'>
"""
print(data.shape) #returns tuples
"""
(2, 3)
#in a analogy to say (no. of lists, no.of items in the list)
"""
print( np.zeros((2,3)) ) # remember double brackets
#np.zeros((0,4)) returns array([], shape=(0, 4), dtype=float64)
"""
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
"""
print( np.ones((2,3)) ) # remember double brackets
"""
[[ 1.  1.  1.]
 [ 1.  1.  1.]]
"""
array = np.arange(10) #generates a list (not python list) of int upto 9
print(array)
"""
[0 1 2 3 4 5 6 7 8 9]
"""
print(type(array))
"""
<class 'numpy.ndarray'>
"""
print(array[1:5])
"""
[1 2 3 4]
"""
array[3:9] = 10
print(array)
"""
[ 0  1  2 10 10 10 10 10 10  9]
"""
