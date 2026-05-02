# python Dates -- date in python is not a data type of its own, but it can import a 
# module named datetime to work with dats as date object
import datetime
x=datetime.datetime.now()
print(x)

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) # returns the day of week

# creating Date objects
# to create a date, we can use the dattime() class(constructor) of datetime module
# datetime()  class requires yr,month,day to create a date
import datetime
x=datetime.datetime(2026,5,2)
print(x)

#the strftime() method
# the datetime object has a method for formatting date objects into readable strings
import datetime
x=datetime.datetime(2026,5,2)
print(x.strftime("%B")) # returns month name



