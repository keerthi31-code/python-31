#append items to add an item to the end of list we use append() method
thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

#insert items -- to insert an item at a specified index we use insert() mathod
thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
thislist.insert(2,"blue berry")
print(thislist)

#extend list-- to append(add) elenemts from another list to current list, we use extend() method 
thislist=["keerthi", "navya"]
anotherlist=["manasa","aashritha","sriya"]
thislist.extend(anotherlist)
print(thislist)

thislist=["idly","dosa"]
secondlist=["poori","vada"]
thislist.extend(secondlist)
print(thislist)

#add any iterable the extend() method not only for append list but also can add any iterable objects (tuples,sets,dictionaries)
thislist=["mom","dad"]
thistuple=("son","daughter")
thislist.extend(thistuple)
print(thislist)
