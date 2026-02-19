#loop through a dictionary -- by using for loop -- it only returns the keys of dictionary
thisdict={
    "name":"keerthi",
    "age":21
}
for x in thisdict:
    print(x)

#but there are methods to return the values 
thisdict={
    "name":"keerthi",
    "age":21
}
for x in thisdict:
    print(thisdict[x])  

thisdict={
    "name":"keerthi",
    "age":21
}
for x in thisdict.keys():
    print(x)

#loop through both keys and values the items() method
thisdict={
    "name":"keerthi",
    "age":21
}
for x, y in thisdict.items():
    print(x, y)