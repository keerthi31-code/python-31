# scope means where a variable can be accessed in a program
 # python mainly has 4 types LEDB Rule
#local, enclosing,global,builtin
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