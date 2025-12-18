#Number methods
'''
abs()
ceil()
floor()
round()
exp()
log()
log10()
max()
min()
pow()
sqrt()

#absolute method when ever there is negative value by using abs() method will convert it to positive value
num=-5
print("the absolute value is:",abs(num))
x=-3+4j
print(abs(x)) # by using magnitude formula will get answer

#ceil methods returns the nearest largest integer value
#7.7---8
import math
y=45.8
print(math.ceil(y)) #math is the module we have to import so that we can perform all mathametical functions
z=22.3
print(math.ceil(z))
b=9.0001
print(math.ceil(b)) #becoz of nearest largest value
c=25
print(math.ceil(c)) #no decimal point so it give output as int
d=-25.8
print(math.ceil(d))# it works on floating points (-25) > (-26)

#floor functions returns to the nearest smallest integer value
e=33.3
print(math.floor(e))

r=45.9
print(math.floor(r))

#so ceil and floor doesn't work on complex numbers

import math
num1=-15
num2=2.3
print(abs(num1)+math.ceil(num2))

#round - after decimal point if the value is > 5 the result is nearest largest number
# if value is =< 5 the result is nearest smallest number

j=float(input("enter the value:"))
print(round(j))

k=8.6
print(round(k))

E=-89.5
print(round(E))

#doesn't work on complex numbers

F=9.645
print(round(F,2))

#exponential method returns e raised to the power of x
import math
num1=3
print(math.exp(num1))
num2=5
print(math.exp(num2))

#log() method returns natural logarithm of x (to the base e)
num3=10
print(math.log(num3))
# so log function doesn't work on negative numbers and complex 

#LOG10() method returns the base-10 logarithm of x
num4=1
print(math.log10(num4))
num=10
print(math.log10(num))


#max method returns the largest value among the given arguments
#max is built in method so no need to import any module
abc=(2,3,4,6,7,8)
print(max(abc)) #prints the max value from the tuple

#min function returns the smallest value among the given arguments
efg=[23,67,90,5,78]
print(min(efg))

#pow() method returns the value of x to the power of y
#we need to import math module to use pow() method
import math
pqr=(2,3) #it contains the values as 1st number is base and 2bd number is power
print(math.pow(pqr[0],pqr[1]))
stu=(2.22,12)
print(math.pow(stu[0],stu[1]))
#expcept complex numbers all numbers will execute
'''

#sqrt function returns the square root of a number
import math
a=16
print(math.sqrt(a))

b=23.8
print(math.sqrt(b))

c=-25
print(math.sqrt(c))
#sqrt function doesn't work on negative numbers and complex numbers.