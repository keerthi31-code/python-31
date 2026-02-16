# to remove items use the remove() or discard() method
thisset={"a","b","c"}
thisset.remove("b")
print(thisset)

thisset={"apple","banana","kiwi"}
thisset.discard("kiwi")
print(thisset)

# the pop() method to remove an item,
#  but this method will remove a random item, so you cannot be sure what item that gets removed.
#The return value of the pop() method is the removed item.
thisset={"apple","banana","kiwi"}
x=thisset.pop()
print(x)
print(thisset)