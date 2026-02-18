thisdict={  #access the items of a dict by referring the key name,inside [] brackets
    "name":"keerthi",
    "age":21,
    "course":"python"
}
x=thisdict["name"]
print(x)

#another method for accessing the item get()
thisdict={
    "name":"keerthi",
    "age":21,
    "course":"python"
}
x=thisdict.get("age")
print(x)

#getkeys -- keys() method will return a list of all the "keys" in the dictionary
#any changes done to the dictionary will be reflected in the keys list
chocolate={
    "brand":"amul",
    "flavour":"dark chocolate",
    "year":1990
}
x=chocolate.keys()
print(x) #before change
chocolate["color"]="brown"
print(x)#after change 

#checking if key exists
thisdict={
    "brand":"amul",
    "flavour":"dark chocolate",
    "year":1990
}
if "cost" in thisdict:
    print("yes,is one of the keys in thisdict " )
else:
    print("no")