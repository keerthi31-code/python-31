#removing items 
#pop() removes the item with the specified key name:
thisdict={
    "name":"keerthi",
    "age":21,
    "branch":"csm"

}
thisdict.pop("age")
print(thisdict)

#popitem() removes the last inserted item
thisdict={
    "name":"keerthi",
    "course":"python"
}
thisdict.popitem()
print(thisdict)

#del keyword removes the item with specified key name
thisdict={
    "name":"keerthi",
    "course":"python",
    "year":2026
}
del thisdict["year"]
print(thisdict)

#clear() method empties the dictionary
thisdict={
    "name":"keerthi",
    "age":21,
    "course":"python"
}
thisdict.clear()
print(thisdict)