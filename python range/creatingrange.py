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