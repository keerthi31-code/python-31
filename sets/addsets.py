#by using add() method can add items to a set
thisset={"a","b","c"}
thisset.add("k")
print(thisset)

#add sets -- to add items from another set into current set, need to use update() method
thisset={"a","b","c"}
myset={"d","e","f"}
thisset.update(myset)
print(thisset)

thisset={"navya","manasa","sriya"}
myset={"keerthi","aashritha"}
thisset.update(myset)
print(thisset)

#add any iterable -- The object in the update() method does not have to be a set, it can be any iterable object 
# (tuples, lists, dictionaries etc.)
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)