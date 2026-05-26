'''
Python Try Except
the try block is used to test a block of code for errors
except block -- handle the errors
else block -- execute code when there is no error
finally -- execute code, regardless of the result of the try -- escept blocks

'''
"""
Exception Handling
error means exception , when exception occurs python will normally stop and generate an error message
this exception can be handled using the try statement

"""

try:
    print(x) # try block generate an exception , because x is not defined
except:
    print("An Exception occured")    

#Since the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error:

# Many exceptions
# can define as many exception blocks as wat 
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")    


#Else 
# Else keyword to define a block of code to be executed if no errors were raised
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong") 


# Finally -- the finally block, if specified will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' os finished'")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")                       










