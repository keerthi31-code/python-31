#list comprehension Based on a list of fruits, you want a new list, 
# containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a
#  for statement with a conditional test inside:
#With list comprehension you can do all that with only one line of code:

fruits=["apple","banana","mango","guava","sapota"]
newlist=[x for x in fruits if "n" in x]
print(newlist)

#condition
fruits=["apple","banana","mango","guava","sapota"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)

#iterable
newlist=[x for x in range(10)]
print(newlist)

#with condition
newlist=[x for x in range(10) if x<5]
print(newlist)