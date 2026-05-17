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

#06/may
class employee:
    def __init__(self,name):
        self.name=name
class developer(employee):
    def __init__(self,name,prog_lang):
        super().__init__(name) # calls the parent class
        self.prog_lang=prog_lang
d1=developer("keerthi", "python")
print(d1.name)
print(d1.prog_lang)      

class animal:
    def shout(self):
        print("animal is shouting")
class dog(animal):
    def sound(self):
        print("BOW")
class cat(animal):
    def sound(self):
        print("MEOW")  
c1=cat()
c1.shout()
c1.sound()
d1=dog()
d1.sound()

# Abstract method
from abc import ABC, abstractmethod
class area(ABC):
    @abstractmethod
    def shape(self):
        print("Area")
class circle(area):
    def shape(self):
        r=2
        print(3.14*r*r)
class rectangle(area):
    def shape(self):
        l=4
        b=5
        print(l*b)
r1=rectangle()
r1.shape()
c1=circle()
c1.shape()


# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print("vehicle")
# class car(vehicle):
#     def start(self):
#         print("i'm car")
# class bike(vehicle):
#     def start(self):
#         print("i'm bike")    
# b1=bike()
# b1.start()
# c1=car()
# c1.start()
# v=vehicle()
# v.start()
           
# polymorphism
#Same method name behaves differently for different objects.
#Can be method overloading or method overriding.
# create a parent class animal having sound as a method, child class dog having as a method
#  -- method overriding having same method but behave differently depend on object
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("dog sounds Bow bow")   

a=animal()
a.sound()
d=dog()
d.sound()        


# p-employ, ch- developer, ch- manager classes---work method
class employee:
    def work(self):
        print("im employee")
class developer(employee):
    def work(self):
        print("works on code")
class manager(employee):
    def work(self):
        print("manages team")
ma=manager()
e=employee()
d=developer()
ma.work()
e.work()
d.work()                        

#p-payment, ch-upi, ch-card---method=pay(self, amnt)

class payment:
    def pay(self, amount):
        print("payment processing")
class upi(payment):
    def pay(self, amount):
        print("paid by upi", amount)
class card(payment):
    def pay(self, amount):
        print("paid by card", amount)
c=card()
u=upi()
p=payment()
p.pay(500)
c.pay(5000)
u.pay(1000)        



#Create a base class Animal.Subclasses:
# Dog Cat Each class should implement: sound method()
# Expected:Dog → "Bark"Cat → "Meow"
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound (self):
        print("Meow")       
c=cat()
d=dog()
a=animal()
c.sound()
d.sound()
a.sound()

#Create base class:Employee
# Subclasses:Manager Developer Intern 
# Each employee has: name salary 
# Manager gets bonus salary. 
# Developer gets project allowance.
# Intern gets stipend.
class Employee:
    def __init__(self ,name, salary):
        self.name=name
        self.salary=salary
    def calculate_salary(self):    
        print("Employee",self.salary)
class manager(Employee):
    def calculate_salary(self):
        bonus=20000
        total=self.salary+bonus
        print(self.name, "Manager salary:",total)
class developer(Employee):
    def calculate_salary(self):
        allowance=10000
        total=self.salary+allowance
        print(self.name, "Developer salary:", total)
class intern(Employee):
    def calculate_salary(self):
        stipend=5000
        total=self.salary+stipend
        print(self.name, "Intern salary:", total)
m=manager("keerthi", 40000)
d=developer("navya",35000)
i=intern("lavanya",15000)                
m.calculate_salary()
d.calculate_salary()
i.calculate_salary()
            
        
