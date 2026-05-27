
# if file exist file overwrites
# if file doesn't "w" creates if
file=open("k1.txt","w")
file.write("hi i'm keerthi")
file.close()

with open("hi.txt", "w") as file:
    file.write("hi everyone")

file=open("k1.txt","r")
print(file.read())
file.close()