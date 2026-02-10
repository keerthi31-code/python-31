#sort lists alphanumerically -- it sorts the list alphanumerically, ascending, by default
thislist=["orange","mango","kiwi","pineapple","banana"]
thislist.sort()
print(thislist)

thislist=["keerthi","manasa","navya"]
thislist.sort()
print(thislist)

#sorting numerically
thislist=[100,50,65,78,34]
thislist.sort()
print(thislist)

#sort Descending-- the keyword argument reverse=true
thislist=["orange","mango","kiwi","pineapple","banana"]
thislist.sort(reverse=True)
print(thislist)

thislist=[100,87,54,98,107]
thislist.sort(reverse=True)
print(thislist)

#customize sort  function -- key = function
def myfunc(n):
  return abs(n - 23)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#case insensitive sort -- sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["Banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#built-in function
thislist=["banana","Orange","Kiwi","cherry"]
thislist.sort(key=str.lower)
print(thislist)

#reverse order
thislist=["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)