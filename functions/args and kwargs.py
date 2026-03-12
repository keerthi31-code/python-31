#what is *args
#it allows a function to accept any number of positional arguments
def add(a,b):
    return(a+b)
print(add(5,6))
#if we want to add many numbers that's where *args used
def add(*numbers):
    print(numbers)
add(1,2,3,4,5)    #*args stores arguments in tuple


def add(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print(sum)
add(1,2,3,4,5) 

def greet(*names):
    for n in names:
        print("hello",n)
greet("keerthi","navya")     

# *args collects the positional arguments

# KWARGS **kwargs allows a function to accept any number of keyword arguments
#this arguments are stored in a dictionary
def info(**data):
    print(data)
info(name="keerthi",age=21)    

#using loop with **kwargs
def info(**data):
    for key,value in data.items():
        print(key,":",value)
info(name="keerthi",age=21,city="hyd")        




    