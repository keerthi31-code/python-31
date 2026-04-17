# Python Iterators
# an iterator is an object that contains countable number of values -- traverse through all the values

#Iterator vs Iterable
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:

mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#strings are also iterable objects, containing a sequence of characters
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr="keerthi"
myit=iter(mystr)
print(next(myit))