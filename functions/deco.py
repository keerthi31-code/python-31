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
    
