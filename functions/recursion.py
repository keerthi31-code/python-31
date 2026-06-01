#recursion is when function calls itself
def print_numbers(n):
    if n==0:
        return
    print(n)
    print_numbers(n-1)
print_numbers(5)    

def printnumbers(n):
    if n==0:
        return
    print(n)
    printnumbers(n-1)
printnumbers(3) 

def sumNums(n):
    if n==1:
        return 1
    sum=n+sumNums(n-1)
    return sum
print(sumNums(4))    