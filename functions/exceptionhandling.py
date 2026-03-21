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

