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
c1.parent()    

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

# multilevel -- child class, parent class, grand parent class
class grandparent:
    def grandpa(self):
        print("im grand pa")
class parent(grandparent):
    def parent(self):
        print("im father")
class child(parent):
    def children(self):
        print("im children")     
c1=child()
c1.parent()
c1.grandpa()    

# hierarical --one parent multiple childrens
class parent:
    def father(self):
        print("im father")
class child1(parent):
    def children1(self):
        print("im elder child")
class child2(parent):
    def children2(self):
        print("im child2 ")    
c1=child1()
c1.father()
c2=child2()
c2.father()