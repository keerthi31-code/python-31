#there are several ways to join two or more sets 
#union() method returns a newset with all items from both sets
set1={"a","b","c"}
set2={1,2,3,4}
set3=set1.union(set2)
print(set3)
 # "|" operator is used to instead of union()
set1={"keerthi","navya"}
set2={15,41} 
set3=set1|set2
print(set3)

#join multiple sets -- 
set1={"a","b","c","d"}
set2={1,2,3,4}
set3={"navya","mansa"}
set4={"keerthi","sriya","aash"}
myset=set1.union(set2,set3,set4)
print(myset)

set1={"a","b","c","d"}
set2={1,2,3,4}
set3={"navya","mansa"}
set4={"keerthi","sriya","aash"}
myset=set1|set2|set3|set4
print(myset)

#join a set and a tuple
x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)

a={"navya",}
b=("keerthi",)
c=a.union(b)
print(c)

#update() method inserts all items from 1 set to another
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)

set1={"hp","dell","asus"}
set2={74000,76000,78000}
set1.update(set2)
print(set1)

#intersection() method will return a new set, that only contains the items that are present
#in both sets
set1={"apple","banana","kiwi"}
set2={"microsoft","apple","google"}
set3=set1.intersection(set2)
print(set3)

#use "&" to join two sets
set1={"apple","banana","kiwi"}
set2={"microsoft","apple","google"}
set3=set1&set2
print(set3)