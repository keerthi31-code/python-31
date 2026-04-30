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

#looping through an interator
mytuple=("keerthi","navya","choti")
for x in mytuple:
    print(x)

mytuple=[1,2,3,4,5,6]
for x in mytuple:
    print(x)

mytuple=["keerthi",20,"Python"]  
for x in mytuple:
    print(x)  


#create an iterator
#the __iter__() method acts similar,
# you can do operations (initializing etc.),
#  but must always return the iterator object itself.

#The __next__() method also allows
#  to do operations, and must return the next item in the sequence.

class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=mynumbers()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#stop iteration 
#To prevent the iteration from going on forever, we can use the StopIteration statement.

#In the __next__() method, 
# we can add a terminating condition to raise an error if the iteration is done a specified number of times:
class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=mynumber()
myiter=iter(myclass)
for x in myiter:
    print(x)        
