# a lambda function is a small one line function
square=lambda x: x*x
print(square(5))

#structure lambda arguments: expression
lambda x: x+10
# why --- for short code, used in map(),filter()
#map() function -- it applies a function to every element in a list
num=[1,2,3,4]
result=list(map(lambda x:x*2,num))
print(result)

#filter() function
#it selects elements based on a condition
num=[1,2,3,4,5]
result=list(filter(lambda x: x%2==0, num))
print(result)

num=[1,2,3,4,5,6,7,8,9]
result=list(filter(lambda x: x%3==0,num))
print(result)

#recusion -- a function calling it self
def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
print(fact(4))

def palin(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palin(s[1:-1])
print(palin("keerthi"))

def palin(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return palin(s[1:-1])
s=input("enter a string: ")
if palin(s):
    print("palindrome")
else:
    print("not palindrome")    
    
