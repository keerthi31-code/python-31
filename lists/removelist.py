#remove() removes specified item
thislist=["apple","banana","kiwi"]
thislist.remove("banana")
print(thislist)

#if there are repeted items present then it removes the frst occurance of item
thislist=["apple","banana","kiwi","banana"]
thislist.remove("banana")
print(thislist)

#removing the specified index by using pop() method
thislist=["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

# if do not specify the index then it will removes the last item
thislist=["apple","banana","kiwi"]
thislist.pop()
print(thislist)

#del is used to removes the item of specified index
thislist=["apple","banana","cherry"]
del thislist[0]
del thislist[1]
print(thislist)

thislist=["apple","banana"]
del thislist()
print(thislist)

#clear the list -- clear() method emties the list
# remains but no content
thislist=["apple","banana"]
thislist.clear()
print(thislist) 

thislist=["keerthi","manasa","navya","sriya","Aash"]
thislist.clear()
print(thislist)