# exception handling -- to avoid program crashes
# try:
#     a=int(input())
#     print(10/a)
# except: 
#     print("error occured")

# QUESTIONS

def fact(n):
    if n==1:
        return 1
    return n*fact( n-1)
print(fact(5))

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
                #5+4, 4+3, 3+2, 2+1, 1+0

print(sum(5))

def isPowerOfFour(n):
        if n<=0:
            return False
        while n%4==0:
            n=n//4
        return n==1
print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1)) 

def reverse_string(n):
    if len(n)==0:
         return n
    return n[-1]+reverse_string(n[:-1])

print(reverse_string("keerthi"))   

# def fib(n):
#     if n==1:
#         return 0
#     if n==2:
#          return 1  
#     return fib(n-1)+fib(n-2)
# n=int(input("enter the number: "))
# for i in range(1,n+1):
#     print(fib(i), end=" ")



def sum_numbers(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(sum_numbers(5))  

def sumDigits(n):
    if n==0:
        return 0
    return n%10+sumDigits(n//10)
print(sumDigits(123))

def sum_digits(n):
    total = 0
    while n > 0: #123>0
        total += n % 10 # 123%10
        n = n // 10 # 123=123//10
    return total

print(sum_digits(123))

def product(n):
    total=1
    while n>0:
        total *=n%10
        n=n//10
    return total    
print(product(123))