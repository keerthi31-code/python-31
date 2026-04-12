# the built-in range() function returns an immutable sequence of numbers,
# it cannot be modified after it is created
#range(start, stop, step) # it can be called with 1,2or3 arguments
# call range() with one argument
#If the range function is called with only one argument, the argument represents the stop value.
x=range(10)
print(x) # range(0, 10)
print(list(x))

#call range( with two arguments
# 1st arguments represents "start" and 2ng argument is "stop"
x=range(3, 10)
print(list(x))

#call range() with three arguments
# the 3rd arg represents step
x=range(3,10,2)
print(list(x))

#using ranges
# ranges are often used in for loops 
for i in range(10):
    print(i)

# using list to display ranges
#range is not directly displayed, so range should convert to lists for display
print(list(range(5)))
print(list(range(1,6)))
print(list(range(3,10,2)))

#slicing ranges
# to extract a subsequence
r=range(10)
print(r[2])
print(list(r[:3]))

x=range(8)
print(x[6])
print(list(x[3:]))

#membership testing
#ranges support membership testing with the 'in' operator
x=range(0,10,2)
print(6 in x) # returns True
print(7 in x) #returns False

#length
#ranges support len() to get the no. of elements in range

x=range(0,10,2)
print(list(x))
print(len(x))