#generators are functions that can pause and resume their execution
# when a generator dunction is called, it returns a generator object which is an iterator
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)    
