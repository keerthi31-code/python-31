#dictionaries are used to store data values in key:value pairs
#dictionary is a collection which is ordered changable and not allows duplicates
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(thisdict)

thisdict={
    "name":"keerthi",
    "course":"python"
}
print(thisdict)

hisdict={
    "name":"keerthi",
    "course":"python"
}
print(thisdict["course"])

#dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#duplicates not allowed
#dictionaries cannot have two items with the same key
thisdict={
    "name":"keerthi",
    "course":"python",
    "year": 1964,
    "year":2020
}
print(thisdict)

#dictionary length
thisdict={
    "name":"keerthi",
    "course":"python"
}
print(len(thisdict))

#dictionary items - data types
#the values in dictionary items can be of any data types
thisdict={
    "name":"keerthi",
    "course":"python",
    "year":1964   
}
print(type(thisdict))

#dict() constructor
#it is also possible to use the dict() constructor to make a dictionary
thisdict=dict(name="keerthi",age=21,country="india")
print(thisdict)


