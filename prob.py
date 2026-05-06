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

## 5/may
#1st -- basic inheritance
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def Dog(self):
        print("BOW BOW") 
d1=dog()
d1.sound() 
d1.Dog()
#2nd
# method overriding same method in parent class and child class
class Bird:
    def fly(self):
        print("Bird can fly")
class parrot(Bird):
    def fly(self):
        print("Parrot can fly high")
p1=parrot()
p1.fly()            

#3rd -- 
class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def display(self):
        print("student name is", self.name)
s1=student("keerthi")
s1.display()   
# 4th
class vehicle:
    def start(self):
        print("Vehicle started")
class Bike(vehicle):
    pass  # here we reusing the parent class without changing anything
b1=Bike()
b1.start()        

                

