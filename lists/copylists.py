#copy a list -- we use copy() method to copy a list
thislist=["keerthi","Aashrith","navya"]
mylist=thislist.copy()
print(mylist)

# another method is list() which is also used to copy list
thislist=["akhila","pavani","keerthi"]
mylist=list(thislist)
print(thislist)

# by using slice-- ":" operator we copy list
thislist=["python learning"]
mylist=thislist[:]
print(mylist)
