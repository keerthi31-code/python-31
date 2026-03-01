# a function is a block of reusable code that performs a specific task
#Instead of writing the same code again and again, we put it inside a function and call it whenever needed.
#why do we need functions
#avoid repeating code
#make code clean and readable
#break big problems into smaller parts

def my_function():
    print("hello from a function")
my_function() #to call a function, we its name and parantheses

# we can call the same function multiple times
#Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32)*5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#return values --When a function reaches a return statement, it stops executing and sends the result back
def get_greeting():
    return"hello"

message = get_greeting()
print(message)

#using thre return value directly
def get_greet():
   return"hi"
print(get_greet())

#the pass statement -- Function definitions cannot be empty
# so need to create a function placeholder without any code, use the pass statement:
def my_funtion():
    pass

### function problems ###
def add(x,y):
    a=x
    b=y
    c=a+b
    return (c)
result=add(2,3)
print(result)
result=add(10,87)
print("result is ",result)  
result=add(5,6)
print("the result",result)

def myfunc():
    return "hello"
print(myfunc())

def myfun():
    return("keerthi","python")
print(myfun())

def my_function(age):
    if age > 18:
        return "major"
    else:
        return "minor"
print(my_function(20))    
print(my_function(17))
print(my_function(29))

def func(num):
    return num*num
print(func(5))

def greater(x,y):
    a=x
    b=y
    if a>b:
        return a
    else:
        return b
print(greater(10,20))

def is_even(n):
    return n%2==0
print (is_even(2))
print(is_even(45))

def square(n):
    return n*n
print(square(2.5))

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(5,7))    


def factorial(n):
    result=1
    for i in range(1, n+1):
        result=result*i
    return result
print(factorial(5))    
    
     

    