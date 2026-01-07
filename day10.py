x = int(input("enter the value :"))
if x % 3==0:
 print("A")
elif x%6==0:
 print("B")
else:
 print("c")
 

marks = int(input("enter the marks:"))
if marks >=40:
  print("pass")
if marks >=75:
 print("distinction")
 

num=int(input("enter the number :"))
if num%2==0:
   print("positive even ")
if num%2!=0:
   print("positive odd")
else:
 print("not positive")


age = int(input("enter your age:"))
if(age>18):
 print("Adult")
elif (age>=60):
  print("Senior")
else:
 print("Minor")
 

x=int(input("enter the numbr:"))
if(x==10):
    print("ten")
elif(x>5):
    print("greater than five")
elif(x>8):
    print("greater than eight")
else:
    print("small")

    

password=input("enter the password:")
if password:
    print("valid")
else:
    print("Invalid")


num =int(input()) 
if num == 0:
    print("zero")
elif num >0:
    print("positive")
else:
    print("negative")