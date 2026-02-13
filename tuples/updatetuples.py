x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#once a tuple is created , it cannot change its values. so for updateding the tuple first we have to convert the tuple to list. change the list, and convert again into tuple.

x=("keerthi","navya","manasa")
y=list(x)
y[2]="aashritha"
x=tuple(y)
print(x)

#add items -- Convert into a list
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

# Add tuple to a tuple
thistuple=("apple","banana","cherry")
y=("orange",)
thistuple +=y
print(thistuple)

#Tuples are unchangeable, so it cannot remove items from it, again converting it to list and removing and convert liat to tuple
thistuple=("apple","banana","cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple) 