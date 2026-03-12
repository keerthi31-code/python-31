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


    