#change values-- changing the value of a specific item by referring to its key name:
thisdict={
    "name":"keerthi",
    "age":21,
    "course":"python"
}
thisdict["course"]="java"
print(thisdict)

thisdict={
    "brand":"amul",
    "flavour":"dark chacolate",
    "year":1990
}
thisdict["year"]=2000
print(thisdict)

#update dict -- update() method will update the dictionary with the items from the given argument
thisdict={
    "name":"keerthi",
    "age":21,
    "course":"java"
}
thisdict.update({"course":"python"})
print(thisdict)

chocolate={
    "brand":"amul",
    "flavour":"milk chocolate",
    "cost":200
}
chocolate.update({"cost":249})
print(chocolate)