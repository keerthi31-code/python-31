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

