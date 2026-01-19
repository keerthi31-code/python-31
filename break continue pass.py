# av=5

# x= int(input("how many candies you want ?"))

# i=1
# while i<=x:
#     if i>av:
#         print("Out of stock")
#         break
#     print("candy")
#     i+=1
# print("Bye")    


# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         continue
#     print(i)

# print("Bye")    


#pass
# for i in range(1,101):
#     if(i%2!=0):
#       pass

#     else:
#        print(i)
# print("bye")    


#1
# while True:
#  x=int(input("enter the value: "))
#  if x<0:
#   print("you entered the positive value")
#   break
# print("stops! you entered negative value")

#2
# for i in range (1,101):
#   if i%7==0 and i%11==0:
#    break
#   print(i) 


#3
# x="python"
# for i in x:
#   if i in 'aeiou':
#     print("vowel found:",i)
#     break
#   print("checked:", i)

  #4
# correct_password="keerthi12345"
# while True:
    
#   x=input("enter the passwords:")
#   if x==correct_password:
#       print("success message")
#       break
#   else:
#       print("wrong try again")

 #5
#  #contiue

# for i in range(1,51):
#     if i % 5== 0:
#      continue 
#     print(i)

#6
# numbers =[2, 3, 5, -6, -10, 45, -9]

# for num in numbers:
#     if num < 0:
#      continue 
#     print(num)

#7
# x= "keerthi is good girl" 
# for ch in x:
#     if ch==" ":
#      continue 
#     print(ch)

#8
# y=input("enter the string")

# for ch in y:
#    if ch==" ":
#        continue
#    print(ch) 
      
#9
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
# for num in numbers:
#     if num%2==0:
#         continue
#     print(num)

#10
# marks= [70,35,89,"A",55,75,"A",90,"A"]
# for i in marks:
#     if i=="A":
#       continue
#     print(i)
 #11
# n=int(input("enter the number of students :"))
# for i in range(1, n + 1):
#     mark = int(input("enter marks for student{i}(-1 if absent)"))
#     if mark==-1:
#         continue
#     print("Marks",mark)
 
 #Pass
 #12
# for i in range(1,7):
#     pass 

#13
#def demo():
   # return

#14
# x=int(input("enter a number :"))

# if x>0:
#     pass
# elif x==0:
#     print("zero")
# else:
#     print("negative")

#15
# class Test:
#     pass

# t=Test()
# print("Class created successfully")

# class Student:
#     pass
# s=Student
# print("hi")

# class Employee:
#     def calculate_salary(self):
#         pass
#     def generate_report(self):
#         pass

#16
# num=int(input("enter the value :"))
# for i in range(1,num+1):
#     if i >5:
#         pass
#     else:
#         print(i)

##Mixed concept questions
#17
# for i in range(1,101):
#     if i%20==0:
#      break
#     elif i%3==0:
#      continue
#     else:
#       print(i)
#18
user=["keerthi","manasa"," ","navya","admin","aashritha"] 
for user in user:
   if user=="":
    continue
   if user== "admin":
    break
   if user =="banned":
     pass
   else:
    print(user)

    












      