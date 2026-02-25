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


#default parameter values
def my_function(name="friend"):
    print("hello",name)
my_function("keerthi")
my_function("navya")
my_function()    

#keyword arguments -- can send arguments with the key = value syntax
def my_function(animal, name):
    print("i have a",animal)
    print("my",animal + "'s name is", name)
my_function(animal="dog", name="buddy")    

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

#positional argument
#when calling a function with arguments without using keywords, they are called positional argmts
def my_function(animal, name):
    print("i have a", animal)
    print("my", animal + "'s name is", name)
my_function("dog","buddy")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "cat")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Hash", "cat")

