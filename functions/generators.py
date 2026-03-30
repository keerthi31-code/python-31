#generators are functions that can pause and resume their execution
# when a generator dunction is called, it returns a generator object which is an iterator
def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)    

 #generators allow you to iterate over data without storing the entire dataset in memory
 # instead of using return, generator use the yiels keyword


#the yield keyword keyword
# yield keyword is what makes a function a generator
# when yield is encountered, the function's state is saved, and the value is returned.
# the next time the generator is called, it continues from where it left off

## generator that yields numbers
def count_upto(n):
    count=1
    while count<=n:
        yield count
        count +=1
for num in count_upto(5):
    print(num)        

# unlike generators which terminates the function, yield pauses it and can be called multple times

#GENERATORS SAVES MEMORY
#generators are memory efficient because they generate values on-the-fly instead of storing everything in memery
def large_sequence(n):
    for i in range(n):
        yield i
gen = large_sequence(1000000) 
print(next(gen))
print(next(gen))
print(next(gen))

#using next() with generators
def simple_gen():
    yield "keerthi"
    yield "navya"
    yield "aash"
gen = simple_gen()
print(next(gen))    
print(next(gen))    
print(next(gen))       
