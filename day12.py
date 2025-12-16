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
'''
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