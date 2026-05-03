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

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))