# What is an array
# array is a special varibale, which can hold more than one value at a time
#access the elements of an array
cars=["Ford","Volvo","BMW"]
x=cars[0]
#modify the value of the first array item
cars[0]="toyota"
print(cars)

names=["keerthi","navya","aashritha","mansa","sriya"]
names[1]="choti"
print(names)

#length of an array
# use len() menthod to return the length of array
x=len(cars)
y=len(names)
print(x)
print(y)

#looping array elements
# for in loop tp loop through the elemnets of an array
for x in cars:
    print(x)
for y in names:
    print(y)

#adding array elements
#append()

cars.append("honda")
print(cars)
names.append("navya")
print(names)

# remove array elements -- using pop()
cars.pop(1)
print(cars)

names.pop(5)
print(names)
# remove also used for remove an element
names.remove("mansa")
print(names)

names.remove("keerthi")
print(names)
cars.remove("BMW")
print(cars)