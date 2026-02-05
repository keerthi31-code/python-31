# while loop is mainly concentrates on intialization, condition, increment ot decrement.
# a while loop is used to repeatedly execute a block of code as long as a given condition is True.
#When the condition becomes False, the loop stops, and the program continues with the next statement after the loop.

# i=1
# while i<=5:
#     print("python ",end="")
#     j=1
#     while j<=4:
#         print("learning ",end="")
#         j=j+1
#     print()
#     i=i+1

# #1
# for i in range(1,11):
#     print(i)

#2
# i=1 
# while i<=10:
#     print(i)
#     i=i+1

#3
# for i in range(1,21):
#     if i % 2==0:
#      print(i)

#4
# sum=0
# i=1
# while i<=10:
#     sum +=i
#     i+=1
#     print(sum)

#  #5
# x=["apple","banana","guava"]  
# for i in x:
#     print(i)
# y=[19,45,87] 
# for i in y:
#     print(i)

#6
# num = int(input("enter the number :"))
# #convert negative to positive
# if num<0:
#     num = -num
# count = 0
# if num==0:
#     count=1
# else:
#     while num>0:
#         num=num//10 #removes last digit
#         count += 1
# print(count)        

#7
# for i in range(10,0,-1):
#     print(i)

#8
# num=int(input("enter the positive number :"))
# while num<=0:
#     num = int(input("not positive enter again :"))
#     print("you entered :",num)

#9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num == 5:
#         continue
#     print(num)



## BASIC WHILE LOOP CODE
# i=1
# while i<=5:
#     print(i)
#     i=i+1

# i=1
# while i <=10:
#     if i == 5:
#         break
#     print(i)
#     i=i+1   

# i=0
# while i<5:
#     i+=1
#     if i==3:
#         continue
#     print(i)

# n=int(input("enter the value:"))
# i=1
# while i<=n:
#     print(i)
#     i+=1  

# questions
# i=1
# while i<=10:
#     print(i)
#     i=i+1  


# i=10
# while i>=1:
#     print(i)
#     i=i-1  

# i=2
# while i<=20:
#     print (i)
#     i=i+2 


# i=1
# while i<=20:
#     if i%2!=0:
#      print(i)
#     i+=1

# i=1
# while i<=10:
#    print(5,"x",i,"=",5*i)
#    i+=1    

# n=int(input("enter the number:"))
# i=1
# while i<=n:
#  print(i)
#  i+=1

# num=int(input("enter the digits:")) 
# count=0
# while num!=0:
#  num= num//10
#  count=count+1
# print(count)
 
# n=1234
# rev=0
# while n>0 :
#     x=n%10
#     n=n//10
#     rev=rev*10+x
# print(rev)

# n=int(input("enter the vlaue: "))
# rev=0
# while n>0:
#     x=n%10
#     n=n//10
#     rev=rev*10+x
# print(rev)    

  
# n=34567
# sum_digits=0
# while n>0:
#     x=n%10
#     sum_digits=sum_digits +x
#     n=n//10
# print(sum_digits)  

# n=int(input("enter the digits :"))
# sumofDigits=0
# while n>0:
#     x=n%10
#     sumofDigits= sumofDigits + x
#     n=n//10
# print(sumofDigits)    

# n=int(input("enter the value:"))
# original=n
# rev=0
# while n>0:
#     x=n%10
#     rev=rev*10+x
#     n=n//10

# if original==rev:
#     print("yes palindrome")
# else:
#     print("no")   
# 
# n=370
# original=n
# sum_digits=0
# digits=0
# temp=n

# while temp >0:
#     digits +=1
#     temp=temp//10

# while n>0:
#       digit=n%10
#       sum_digits=sum_digits+(digit** digits)
#       n=n//10  

# if sum_digits==original:
#     print("yes")
# else:
#     print("no")