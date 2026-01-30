
#patterns pattern printing programs where we use loops to print shapes using stars (*), numbers, or characters in a specific order.

# They are mainly used to:
# Understand loops (for, while)
# Practice nested loops
# Learn logic building
# Improve control over rows and columns


# print("#")
# print("#")

# print("# ",end="")
# print("# ",end="")



# for i in range(4):
#  for j in range(4):
#   print("# ",end="")
#  print()

#  for i in range(4):
#    for j in range(i+1):
#     print("#",end="")
#    print() 

# for i in range(4):
#  for j in range(4-i):
#   print("# ",end="")
#  print()  

 
# for i in range(5):
#     for j in range(5-i):
#         print("* ",end="")
#     print()   

# num = int(input("enter the number:"))
# for i in range(num):
#     for i in range(num):
#         print("*",end="")
#     print()    

# num=int(input("enter the number:"))
# for i in range(num):
#     for j in range(i+1):
#         print("*",end="")
#     print()    

# num=int(input("enter the number:"))
# for i in range(num):
#     for j in range(num-i):
#         print("*",end="")
#     print()    


# num=int(input("enter the number:"))
# for i in range(1,num+1):
#     for j in range(1, i+1):
#         print(j,end="")
#     print()     

# num=int(input("enter the number:"))
# for i in range(1,num):
#     for j in range(1,num-i+2):
#         print(j,end="")
#     print()           



#for else
# numbers=[12,7,22,46,87]

# for num in numbers:
#     if num%5==0:
#         print(num)
#         break
# else:
#     print("number not found")   

#prime number in python
# num=10
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")


# num=int(input("enter the number :"))
# for i in range(2,num):
#     if num%2==0:
#         print("not prime")
#         break
# else:
#     print("prime")        


# for i in range(5):
#     for j in range(5-i):
#         print("*",end="")
#     print()  

# num=int(input("enter the number:"))
# for i in range(1,num+1):
#         print(" "*(num-i),end="")
#         print("*"*(2*i-1))
      
# n=5
# for i in range(1,n+1):
#         print(" "*(n-i),end="")
#         print("*"*(2*i-1))


# num=int(input("enter the number:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()           
# 
num = int(input("enetr the number :"))
for i in range(0,num+0):
    for j in range(0,i+0):
        if(i+j)%2==0:
         print(0,end="")   
        else:
           print(0,end="") 
    print()        
