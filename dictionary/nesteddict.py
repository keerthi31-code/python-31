# a dictionary can contain dictionaries, this is called nested dictionaries
family={
    "child":{
        "name":"keerthi",
        "year":2004
    },
    "child2":{
        "name":"dhanu",
        "age":2002
    }
} 
print(family)


child={
    "name":"keerthi",
    "year":2004
}
child2={
    "name":"dhanu",
    "age":2002
    }
myfamily={
    "child":child,
    "child2":child2
}
print(myfamily)