#Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase  # DECORATOR
def myfunction(): #  IS THE FUNCTION THAT GETS DECORATED
    return "Hello Keerthi"
print(myfunction())

def changecase(func):
    def myinner():
        return func().lower()
    return myinner
@changecase 
def myfunction():
    return "HELLO KEERTHI"
print(myfunction())
    
#multiple decorator calls
# a decorator can be called muitiple times, we need to place the generator abouve the function want to decorate
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "hello keerthi"
@changecase
def function():
    return "i'm good!"
@changecase
def other():
    return "How are you?"
print(myfunction())
print(function())
print(other())

# Arguments in the decorated function
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner
@changecase
def myfunction(name):
    return "hello "+name
print(myfunction("keerthi"))

def greet():
    return "hello"
def display(func):
    print(func())
display(greet)    

def outer():
    def inner():
        print("Inside inner function")
    return inner
func=outer()
func()  

#basic decorator structure
def my_decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

# using a decorator 
def say_hello():
    print("hello!")
decorated=my_decorator(say_hello)
decorated()        

# args and kwargs
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner
@changecase
def myfunction(nam):
    return "hello "+nam
print(myfunction("keerthi"))

#decorator with arguments
def changecase(n):
    def changecase(func):
        def myinner():
            if n==1:
                a=func().lower()
            else:
                a=func().upper()
            return a
        return myinner
    return changecase
@changecase(1)
def myfunction():
    return "hello keerthi"
print(myfunction())   
