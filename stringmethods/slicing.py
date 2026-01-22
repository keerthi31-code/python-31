#slicing which means extract part from string 

a="python"
print(a[0:4])
print(a[2:])
print(a[:4])

b="keerthi"
print(b[4:6])
print(b[::-1])

#negative indexing
c="python learning"
print(c[-1])
print(c[-4:-1])

#string methods
#strip is used to remove white spaces
#split is used to split the strings

#string concatenation
v="Muchha"
w="Keerthi"
print(v+" "+w)

#string formatting
age=20
txt=f"my age is {age}"
print(txt)

age1 = 21
text="my age is {}".format(age)
print(text)

#convert strins to other types
x="10"
print(int(x))
print(float(x))

a="learning python" 
print(a.count("n"))
print(a.removeprefix("learn"))
print(a.removesuffix("python"))
