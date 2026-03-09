def greet(name): #name -- parameter, 
    print("hello",name)
greet("keerthi")    #keerthi -- argument

#values are passed in the same order as parameter
def add(a,b):
    print(a+b)
add(5,6)   

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

def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    a=0
    b=1

    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    return b
n=int(input("enter the value:"))
print(fibonacci(n))

