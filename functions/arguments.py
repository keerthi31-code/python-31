# Arguments information can be passed into functions as arguments
# Arguments are specified after the function name, inside the parentheses. 
# can add as many arguments as want, just separated by comma
def my_function(fname):
    print(fname + "csma")
my_function("keerthi")
my_function("navya")
my_function("aash")

#parameter vs Arguments 
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
    print("hello", name)
my_function("keerthi")  # "keerthi" is an argument

#number of arguments 
def my_function(fname, lname):
    print(fname+ " " + lname)
my_function("keerthi","muchha")    