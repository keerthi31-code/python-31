# 23/05/26
class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name:",self.name, "\nmarks:",self.marks)
s=Student("keerthi",95)
s.display()            

class Employee:
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print("Name:", self.name, "Salary:", self.salary)
e=Employee("keerthi", 75000)
e.show_details()

class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self, amount):
        self.__balance+=amount
        print("Deposit:",amount)
    def withdraw(self, amount):
        if amount>self.__balance:
            print("insufficient")
        else:    
            self.__balance-=amount 
            print("withdraw",amount)
    def show_balance(self):
        print("show balance:",self.__balance)
b=Bank(10000)
b.deposit(4000)
b.withdraw(5000)
b.show_balance()                       


class Vehicle:
    def start(self):
        print("im started")
class car(Vehicle):
    def drive(self):
        print("car is started")
c=car()
c.drive() 
c.start()  
v=Vehicle()
v.start()             


class Animal:
    def sound(self):
        print("animal makes sound")
class dog(Animal):
    def sound(self):
        print("BOW-BOW")
class cat(Animal):
    def sound(self):
        print("MEOW") 
c=cat()
d=dog()
c.sound()
d.sound()                       


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

# class Student:
    
#     def _init_(self, name):
#         self.name = name

# s = Student("Ravi")
# print(s.name)

class Animal:
    
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    
    def sound(self):
        print("Dog bark")

d = Dog()
d.sound()

# class Test:
    
#     def _init_(self):
#         self.__value = 100

# t = Test()
# print(t.__value)



class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def grade(self,marks):
        if marks >50:
            print("pass",marks)
        else:
            print("fail")
s=Student("keerthi",98)
s.grade(98)                
