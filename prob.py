
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

