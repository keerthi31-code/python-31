def greeting(name):
    print("hello" + name)
import module
module.greeting(" keerthi")   

#variables in modules
person1={
    "name":"keerthi",
    "age":21,
    "country": "india"
}
import module
a=module.person1["age"]
print(a)

#naming a module -- name the module file whatever, but it must have the file extension .py
# renaming a module -- create an alias when import a module by using as keyword

import module as x
a=x.person1["age"]
print(a)

#built-in modules
#platform module
import platform 
x=platform.system()
print(x)

#using dir() function -- to list all the function names in a module
# the dir() func
import platform
x=dir(platform)
print(x)

# imprt from module -- we can choose to import only parts from a module , by using from keyword
def greeting(name):
    print("hello, " + name )
person2={
    "name":"keerthi",
    "age":25,
    "country":"India"
}  
from module import person1
print(person2["age"])  
