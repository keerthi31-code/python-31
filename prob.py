#oops concept
class student:
    def __init__(self):
        print("student is good")
c1=student()       


class employee: #parent class
    def details(self):
        print("i'm employee")

class developer(employee): #child class
    def coding(self):
        print("i'm developer")
        #access parent class from child class
d1=developer()
d1.details()
d1.coding()

class animal:
    def features(self):
        print("Animal")
class dog(animal):
    def bark(self):
        print("BOW BOW")
        print("4 legs")
d1=dog()
d1.features()    
d1.bark()            


# 4types of inheritance 
#single -- one parent one class
class parent:
    def parent(self):
        print("im parent")
class child(parent):
    def children(self):
        print("im children") 

c1=child()
c1.children()    

# multiple inheritance -- multiple parent , one child
class parent1:
    def father(self):
        print("im father")
class parent2:
    def mother(self):
        print("im mother")
class child(parent1, parent2):
    def child(self):
        print("im children")                
c1=child()
c1.mother()
c1.father()        