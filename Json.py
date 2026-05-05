# Json is a syntax for storing and exchanging data
#JSON is text, written with javaScript object notation
#it is built-in package 
import json
# parse Json string, parse it by using json.loads()
# the result will be a python dictionary
x='{ "name":"keerthi","age":21, "city":"hyd"}'
y=json.loads(x)
print(y["age"])

x='{"name":"keerthi","age":21,"course":"python"}'
y=json.loads(x)
print(y)

#convert from python to json
#json.dumps()
import json
x={
    "name":"keerthi",
    "age":21,
    "city":"hyderabad"
}
y=json.dumps(x)
print(y)

# we convert python objects in to json strings
#dict, list, tuple, string, int, float, true, false,nons
import json

print(json.dumps({"name": "keerthi", "age": 21}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# converting a python object containing all legal data types
import json
x={
    "name":"keerthi",
    "age":21,
    "married":False,
    "pets":None,
     "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

#order the result
print(json.dumps(x, indent=4, sort_keys=True))

#problems 
import json 
x={
    "name":"john",
    "age":21
}
x=json.dumps(x)
print(x)



import json
x='{"city":"Hyderabad","pincode":500001}'
y=json.loads(x)
print(y)

import json
x={"name":"keerthi","age":21}
print(x["age"])

import json
x={"course":"python","duration":"6 months"}
with open("x.json","w") as file:
    json.dump(x, file)
print("data written successfully")    

import json
y={
    "name":"keerthi",
    "age":21,
    "course":"python"
}
#write
with open("y.json","w") as file:
    json.dump(y, file, indent=4)
#read    
with open("y.json","r") as file:
    y=json.load(file)
for keys in y:    
    print(keys) 

# standard level
import json
x={
    "student":{
        "name":"keerthi",
        "marks":[80,90,85]
    }
}
marks=x["student"]["marks"]
avg=sum(marks)/len(marks)
print(avg)