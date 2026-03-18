# a lambda function is a small one line function
square=lambda x: x*x
print(square(5))

#structure lambda arguments: expression
lambda x: x+10
# why --- for short code, used in map(),filter()
#map() function -- it applies a function to every element in a list
num=[1,2,3,4]
result=list(map(lambda x:x*2,num))
print(result)