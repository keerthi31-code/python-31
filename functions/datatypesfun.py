def add(a,b):
    return a+b
print(add(5,3)) # integers

def greet(name):
    print("hello", name)
greet("keerthi") # string

def listsum(lst):
    sum =0
    for i in lst:
        sum+=i
    return sum    

print(listsum([1,2,3,4])) #list

def check(flag):
    if flag:
        print("true value")
    else:
        print("false value")
check(True)            # boolean


def info(name,age,marks):
    print(name)
    print(age)
    print(marks)
info("keerthi",21,85.6)    

#dict
def info(data):
    print(data)
info({"name":"keerthi","age":21})    


#questions
def fun(name):
    return(len(name))
    
print(fun("keerthi"))

def largest_num(lst):
    num=0
    for i in lst:
        if i > num:
            num=i
    print(num)    
largest_num([1,3,4,5,6])  

def smallest_num(lst):
    num=lst[0]
    for i in lst:
        if i<num:
            num=i
    print(num)        
smallest_num([3,6,7,4,9])

def check(flag):
    if flag:
        print("yes")
    else:
        print("no")
check(True)     

def studentdetails(name,age,marks):
    print("Name:",name)
    print("Age:",age)
    print("marks:",marks)
studentdetails("keerthi",21,90)   



    