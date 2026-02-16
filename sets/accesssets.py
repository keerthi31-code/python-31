#it cannot access items in a set by giving index or key
#by using for loop  and for a specified value in a set using in keyword
thisset={"apple","banana","kiwi"}
for x in thisset:
    print(x)

#check if banana is present in the set
thisset={"a","b","c"}
print("b"  in thisset)
print("a" not in thisset) #returns false because it is there in the set
print("z" in thisset)