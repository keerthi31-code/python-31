# scope means where a variable can be accessed in a program
 # python mainly has 4 types LEDB Rule
#local, 
# enclosing,
# global,
# builtin


#local scope
#a variable can be used only inside that function
def fun():
    x=10
    print(x)
fun()  

#global scope
# a variable created outside a function is called a global vaariable
# it can be accessed any where in the program
x=20
def fun():
   print(x)
fun()    


#modifying global variables
#to change the global variable inside a function, must use the keyword
# global
x=10
def change():
    global x 
    x=50
change()
print(x)   

str="keerthi"
def change():
    global str
    str ="manasa"
change()
print(str)    
#without global , python will treat it as a new local variable

#enclosing scope -- a function inside another function can access the outer function variable
def outer():
    x=10
    def inner():
        print(x)
    inner()
outer()        

def outer():
    str="keerthi"
    def inner():
        print(str)
    inner()

outer()  # here str belongs to the outer function


# # built-in scope
# print()
# len()
# max()
# min()
# sum()
x="keerthi"
print(len(x))

