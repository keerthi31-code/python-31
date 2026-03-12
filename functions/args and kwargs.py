#what is *args
#it allows a function to accept any number of positional arguments
def add(a,b):
    return(a+b)
print(add(5,6))
#if we want to add many numbers that's where *args used
def add(*numbers):
    print(numbers)
add(1,2,3,4,5)    
    