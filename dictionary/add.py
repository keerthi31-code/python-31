#adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict={
    "name":"amul",
    "flavour":"dark chocolate"
}
thisdict["cost"]=200
print(thisdict)

#update dictionary
thisdict={
    "name":"keerthi",
    "course":"python"
}
thisdict.update({"education":"btech"})
print(thisdict)
