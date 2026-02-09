#loop lists we loop through the list by using a for loop
# thislist=["apple","banana","cherry"] #we can see that one by one it prints.
# for x in thislist:
#     print(x)

# thislist=["keerthi","navya","mansa"]
# for x in thislist:
#     print(x)    

#loop through the index numbers
#by using the range() and len() functions to create a suitable iterable
# thislist=["aashritha","sriya","narendra","pranay"]
# for i in range(len(thislist)):
#     print(thislist[i])     

# #While loop-- we can loop through by while loop
# # len() function is to determine the length of list, start at 0 and refer through the index number
# thislist=["apple","banana","kiwi"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1   

# thislist=[1,2,3,4,5,6,7,8,9,0]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i+=1

#looping using list comprehension
#a short hand for loop that will print all items in a list
thislist=["keerthi","kitty"]
[print(x) for x in thislist]