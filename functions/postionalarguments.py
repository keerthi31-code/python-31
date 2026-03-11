# def greet(name): #name -- parameter, 
#     print("hello",name)
# greet("keerthi")    #keerthi -- argument

# #values are passed in the same order as parameter
# def add(a,b):
#     print(a+b)
# add(5,6)   

#Functions---------
"""
def fun(): # syntax
    print("Hello")

#print(fun())
fun()
"""

"""
def fun(name):
    return "hello"+' '+ name
n = input()
print(fun(n))

"""
"""
def add(a,b):
    print(a+b)

m,n = map(int,input().split())
add(m,n)
"""
# find the number is even or odd from the given list of numbers
# return true if the str contains vowels 



#Recursion--------------


#fact of a number-----

"""
def f(n):#4,3,2,1,0
    if n==0:
        return 1 
    else:
        return n*f(n-1)# 4*f(3), 3*f(2), 2*f(1),1*f(0)
                           4*6       3*2     2*1      1

n= int(input())#4
print(f(n))#4
fibonacci series
operations
"""

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end="")    
#         c=a+b
#         a=b
#         b=c
#     return b
# n=int(input("enter the value:"))
# fibonacci(n)

# def operations(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div    




# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print(operations(a,b))


# #keyword arguments
# #specifing the parameter names while calling
# def add(a,b):
#     print(a+b)
# add (b=5, a=4)    

# def sub(c,d):
#     print(c-d)
# sub(c=9, d=4)    

#default arguments
#giving a default value to the parameter
# def greet(name="guest"):
#     print("hello",name)
# greet("keerthi")
# greet()   

# def greet(name="welcome"):
#     print("hello",name)
# greet("keerthi") 
# greet()   

# def count(n):
#     count=0
#     for ch in n:
#      count +=1
#     return count
# n=input("enter the name:")    
# print(count(n))

# #arbitary arguments(*args)
# #it is used when don't how many arguments will come
# def add(*numbers):
#    print(sum(numbers))
# add(130,123,345,23)  

# #numbers become tuple

# def greet(*name):
#    for n in name:
#     print("hello",n)
# greet("keerthi","manasa","navya","sriya") 

# #key Arbitrary arguments(**kwargs)
# #used for multiple named arguments

# def info(**data):
#     print(data)
# info(name="keerthi",age=21)   

# def info(**data):
#    print(data)
# info(name="apple",color="red")   

#problems
# def add(a,b):
#    print(a+b)
# a,b=map(int,input().split())
# add(a,b)

# def areaofrectangle(length, width):
#     area=length*width
#     print(area)
# length,width=map(int,input("enter the length,width:").split())
# areaofrectangle(length,width) 

# def max(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# a,b=map(int,input("enter the numbers: ").split())
# print(max(a,b))   

# def student(**data):
#     print(data)
# student(name="keerthi", age=21)   

# def student(**data):
#     for key, value in data.items():
#         print(key,":",value)
# student(name="keerthi",age=21)        
    
# def power(base, exponent):
#     power=base**exponent
#     print(power)
# base,exponent=map(int,input("enter the values: ").split())
# power(base, exponent)    

# def greet(name="guest"):
#     print("hello",name)
# greet("keerthi")  
# greet()

# def interest(principal, rate =5):
#     SI=(principal * rate*1)/100
#     print(SI)
# principal=int(input("enter the principal: "))
# interest(principal)   

# def sum_numbers(*numbers):
#     print(sum(numbers))
# sum_numbers(1,2,3,4)    

# def print_names(*names):
#     for n in names:
#      print("hello",n)
# print_names("keerthi","navya","manasa")       

# def person(**details):
#    for key,values in details.items():
#       print(key, ":",values)
# person(name="keerthi",age=21,city="delhi")      


   # print a string "Hi I'm Bhavanidevi Btech ECE with 80%"
#fun(name="Bhavanidevi",course="Btech", branch="ECE", perc=80%)

#find the prime numbers for the given range---100
   

#functions--define,parameter, return,print,
# *args-if we don't know how many no.of parameters will be pass by the user
"""
def fun(fname,lname):
    print("Hi Im"+" "+fname+" "+lname)
fun(fname='bhavani',lname='devi')

"""
"""
def fun1(fn,ln):
    print("Hlo"+fn+ln)
fun1('how', 'areyou')
"""
"""
def fun(*names):#*args
    return "Hi my name is"+" "+ names[2]

print(fun("a","b","c","d"))


def fun1(**names):
    return "Hi my name is"+" "+names["lname"]
print(fun1(fname="a",lname="b"))
    
"""
def info(**data):
    print("hi i'm",data["name"],data["course"],data["branch"],"with",data["per"])
info(name="keerthi",course="btech",branch="cse ai&ml",per=80)    
        

