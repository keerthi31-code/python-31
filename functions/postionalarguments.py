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
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     a=0
#     b=1

#     for i in range(3,n+1):
#         c=a+b
#         a=b
#         b=c
#     return b
# n=int(input("enter the value:"))
# print(fibonacci(n))

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
def add(a,b):
   print(a+b)
a,b=map(int,input().split())
add(a,b)

def areaofrectangle(length, width):
    area=length*width
    print(area)
length,width=map(int,input("enter the length,width:").split())
areaofrectangle(length,width) 

def max(a,b):
    if a > b:
        return a
    else:
        return b
a,b=map(int,input("enter the numbers: ").split())
print(max(a,b))   


   
   

