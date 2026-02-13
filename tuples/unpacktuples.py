#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits=("apple","banana","cherry")

#in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

#using Asterisk -- he number of variables is less than the number of values,
# we can add an * to the variable name and the values will be assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)