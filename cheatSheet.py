
## Assignment

# Strings
data = 'hello world'
print(data[0])
print(len(data))
print(data)

# Numbers
value = 123.1
print(value)
value = 10
print(value)

# Boolean
a = True
b = False
print(a, b)

# Multiple Assignment
a, b, c = 1, 2, 3
print(a, b, c)

# No Value
a = None
print(a)


## Flow Control

# If and Else 
value = 99
if value >= 99:
	print('That is fast')
elif value > 200:
	print('That is too fast')
else:
	print('That that is safe')
  
# For-Loop
for i in range(10):
	print(i)
  
# While-Loop
i = 0
while i < 10:
	print(i)
	i += 1

	
## Data Structures

# Tuple
a = (1, 2, 3)
print(a)

# List
mylist = [1, 2, 3]
print("Zeroth Value: %d" % mylist[0])
mylist.append(4)
print("List Length: %d" % len(mylist))
for value in mylist:
	print(value)

# Dictionary
mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d" % mydict['a'])
mydict['a'] = 11
print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys())
print("Values: %s" % mydict.values())
for key in mydict.keys():
	print(mydict[key])

## Functions
def mysum(x, y):
	return x + y
# Test Function
print(mysum(1, 3))


## NumPy

# Create Array
import numpy
mylist = [1, 2, 3]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)

# Access Data
import numpy
mylist = [[1, 2, 3], [3, 4, 5]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print("First row: %s" % myarray[0])
print("Last row: %s" % myarray[-1])
print("Specific row and col: %s" % myarray[0, 2])
print("Whole col: %s" % myarray[:, 2])

# Arithmetic
import numpy
myarray1 = numpy.array([2, 2, 2])
myarray2 = numpy.array([3, 3, 3])
print("Addition: %s" % (myarray1 + myarray2))
print("Multiplication: %s" % (myarray1 * myarray2))


## Matplotlib

# Basic Line Plot
import matplotlib.pyplot as plt
import numpy
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('test x axis')
plt.ylabel('test y axis')
plt.show()

# Basic Scatter Plot
import matplotlib.pyplot as plt
import numpy
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x,y)
plt.xlabel('test x axis')
plt.ylabel('test y axis')
plt.show()


## Pandas

# Series
import numpy
import pandas
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)

# Access Data
print(myseries[0])
print(myseries['a'])

# Dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

print("one column: %s" % mydataframe['one'])
print("one column: %s" % mydataframe.one)
