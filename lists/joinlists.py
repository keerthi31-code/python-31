#join lists -- by using + operator we can join or concatenate two or more list
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2 
print(list3)

#another way to join two lists by appending all the items from list2 into list1 , one by one
list1=["apple","sapota"]
list2=["mango","watermelon"]
for x in list2:
    list1.append(x)
print(list1)

list1=["january","february","march"]
list2=["april","may","june"]
for x in list2:
    list1.append(x)
print(list1)    

#extend() method to add list2 at the end of list1
list1=["a","b","c"]
list2=[1,2,3,4]
list1.extend(list2)
print(list1)