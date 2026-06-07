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
            
#Create abstract class:Shape ,Abstract method:area()
#  Subclasses:Circle, Rectangle, Triangle Calculate respective areas.
from abc import ABC, abstractmethod
class shape:
    @abstractmethod
    def area(self):
        print("Area of shape")
class circle(shape):
    def area(Self):
        r=2
        print(3.14*r*r)
class rectangle(shape):
    def area(self):
        l=4
        b=5
        print(l*b)
class triangle(shape):
    def area(self):
        b=3 
        h=5
        print((b*h)/2)

t=triangle()
r=rectangle()
c=circle()
t.area()
r.area()
c.area()             

#Base class:Vehicle 
# Subclasses:Bike Car, Bus, Each vehicle:calculates rent differently, displays vehicle type. Use method overriding.
class vehicle:
    def __init__(self, rent, type):
        self.rent=rent
        self.type=type
    def calculate_rent(self):
        print("velhicle rent",self.rent)
class car(vehicle):
    def calculate_rent(self):
        total=self.rent + 100
        print(self.type,"rent:", total)
class bus(vehicle):
    def calculate_rent(self):
        total=self.rent+200
        print(self.type,"rent:",total)

class bike(vehicle):
    def calculate_rent(self):
        total=self.rent+300
        print(self.type,"rent:",total)
c=car(5000, "car")
b1=bike(2500, "bike")
b=bus(6000, "bus")
c.calculate_rent()
b1.calculate_rent()
b.calculate_rent()
     

#Create abstract class:Payment
# Subclasses:CreditCard Payment,UPI Payment,Wallet Payment,
# Each should implement:pay(amount)
# Use polymorphism to process payments.


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):

    def pay(self, amount):
        print("Credit Card Payment:", amount)

class UPIPayment(Payment):

    def pay(self, amount):
        print("UPI Payment:", amount)

class WalletPayment(Payment):

    def pay(self, amount):
        print("Wallet Payment:", amount)
        
c1 = CreditCardPayment()
u1 = UPIPayment()
w1 = WalletPayment()

c1.pay(1000)
u1.pay(500)
w1.pay(300)
    
#Create base class:Account 
# Subclasses:SavingsAccount, CurrentAccount, 
# Functions:deposit() withdraw() 
# Savings account gives interest. 
# Current account has minimum balance rule    
'''
Encapsulation: wrapping data and methods together inside a class and restrictng direct access to same data
hide internal details
allow access only through controlled methods
eg: ATM machine
You cannot directly access bank balance from inside the machine.
You interact using:
PIN
deposit()
withdraw()
check_balance()
This is encapsulation.

Type	Syntax	Meaning
Public	----  name	--Accessible anywhere
Protected--	 _name	--Should not be accessed directly
Private--	__name	--Strongly restricted
'''
# public variable
class student:
    def __init__(self):
        self.name="Keerthi"
s=student()
print(s.name)        

#private variables (__variable)
class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance
    def show_balance(self):
        print("Name:", self.name, "Balance:", self.__balance)
acc=BankAccount("keerthi",10000)
acc.show_balance()


class Bankaccount:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance
    def deposited_amount(self, amount):
        self.__balance +=amount 
        print("Deposited:",amount)
    def with_draw(self, amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Withdraw:" ,amount)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Balance:", self.__balance)
b=Bankaccount("Keerthi",75000) 
b.deposited_amount(5000)
b.with_draw(25000)
b.check_balance()              

class MobilePin:
    def __init__(self, pin):
        self.__pin=pin
    def checkpin(self, pin):
        if self.__pin ==pin:
            print("correct pin")
        else:
            print("wrong pin")     
    def changepin(self,old_pin, new_pin):
        if self.__pin==old_pin:
            self.__pin=new_pin
            print("pin changed successfully")
        else:
            print("old pin incorrect")
m=MobilePin(3120)
m.checkpin(3120) 
m.changepin(3120, 2004)
m.checkpin(8976)               




# 23/5/26
class Student:
    def __init__(self ,name, marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name:", self.name, "marks:", self.marks)
class student1(Student):
    def display(self):
        print(self.name, self.marks)
class student2(Student):
    def display(self):
        print(self.name, self.marks)
class student3(Student):
    def display(self):
        print(self.name, self.marks)
s1=student1("keerthi", 90) 
s1.display()                  
s2=student2("navya", 85)
s2.display()
s3=student3("lavanya", 79)
s3.display()            


class Rectangle:
    l=10
    b=25
    def area(self):
        print("Area:", self.l * self.b)        
    def parimeter(self):   
        print("parimeter:", (2*(self.l+ self.b)))
r=Rectangle()
r.area()
r.parimeter()



class Mobile:
    def __init__(self, brand, price, color):
        self.brand=brand
        self.price=price
        self.color=color
    def display(self):    
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Color:",self.color)
m1=Mobile("VIVO",25000, "Blue")
m1.display()    

    
class Employee:
    def __init__(self, id, name, salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print("ID:",self.id, "\nName:", self.name, "\nSalary:", self.salary) 
e=Employee("k41","keerthi",75000)   
e.display()   


class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        balance=4000
    def deposit(self):
        deposited_amount=2000
        self.balance=self.balance+deposited_amount
    def withdraw(self):
        withdraw_amount=1000
        self.balance=self.balance-withdraw_amount
    def checkbalance(self):
        print("Balance:",self.balance)
b=BankAccount("keerthi",4000)  
b.deposit()
b.withdraw()
b.checkbalance()      

class Car:
    def __init__(self, company, model, year):
        self.company=company
        self.model=model
        self.year=year
    def car_info(self):
        print("Company:",self.company, "Model:",self.model, "Year:",self.year) 
c=Car("Ford","Mustang",1964)
c.car_info()           

class ATM:
    def __init__(self, name, balance):
        self.name=name
        self.__balance=balance
    def deposit(self, amount):
        self.__balance+=amount
        print("Deposit",amount)
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficinet")
        else:
            self.__balance-=amount
            print("withdraw:", amount)
    def check_balance(self):
        print("checkBalace:",self.__balance)
a=ATM("Keerthi",10000)
a.deposit(2000)
a.withdraw(3000)
a.check_balance()                    
    
class PasswordManager:
    def __init__(self, password):
        self.__password=password
    def set_password(self, new_password):
        self.__password=new_password
        print("password updated")  
    def get_password(self):
        print("get password:",self.__password)

p= PasswordManager(3120)
p.set_password(2004)
p.get_password()           

class Test:
    def __init__(self):
        print("Constructor called")
t=Test()
t.__init__()        


class A:
    
    def show(self):
        print("Class A")

class B(A):
    pass

b = B()
b.show()

arr=[1,2,5,6,7,4.6] 
t=int(input("target:"))
for i in range(len(arr)-1):
    if i in arr:
        t==i
    print("yes")
    break 
else:
    print("no")          
