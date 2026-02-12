#tuples are used to store multiple items, it is a built-in data type used to store collection of data
#Ordered and unchangeadle written in round brackets
mytuple=("apple","banana","cherry")
print(mytuple)

#tuple items are orderd, unchangeable, Allows duplicates
thistuple=("apple","banana","kiwi","apple")
print(thistuple)

#tuple Length
thistuple=("apple","banana","watermelon")
print(len(thistuple))

#create tuple with one item
thistuple=("apple",)
print(type(thistuple))

#tuple items - data types, tuple can contain any data types
tuple1=("apple","banana")
tuple2=(1,2,3,4)
tuple3=(True,False)

#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#tuple() contructor used to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


#check if item exists
 # by using in keyword we can check whether the item are exists
thistuple=("apple","banana","cherry")
if "kiwi" in thistuple:
    print("yes")
else:
    print("no")    