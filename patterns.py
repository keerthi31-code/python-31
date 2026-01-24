
#patterns pattern printing programs where we use loops to print shapes using stars (*), numbers, or characters in a specific order.

# They are mainly used to:
# Understand loops (for, while)
# Practice nested loops
# Learn logic building
# Improve control over rows and columns


print("#")
print("#")

print("# ",end="")
print("# ",end="")



for i in range(4):
 for j in range(4):
  print("# ",end="")
 print()

 for i in range(4):
   for j in range(i+1):
    print("#",end="")
   print() 

for i in range(4):
 for j in range(4-i):
  print("# ",end="")
 print()  

 

