#1
day=int(input("enter the day :"))
match day:
    case 1 if day == 1:
        print("monday")
    case 2 if day ==2:
        print("tuesday")
    case 3 if day == 3:
        print("wednesday")

##2
status = str(input("enter the status :"))
match status.strip():
  case "ok":
    print("success")
  case "error":
   print("failed")
  case _:
   print("unknown status")

   #3
grade = str(input("enter the grade :"))
match grade:
 case "A"|"B":
  print("Good performance")
 case"C":
  print("Average performance")
 case _:
  print("Invalid grade")

#4
choice = int(input("enter the value :"))
match choice:
  case 1:
   print("Start")
  case 2:
   print("Stop")
    
#5

command = str(input("enter the command :"))
match command:
 case _:
  print("Invalid command")

#6
x = int(input("enter the number :"))
match x:
 case n if n>0 and n % 2 ==0:
  print ("positive Even")
 case _:
  print("other number")
  

#7
fruit = str(input("enter the fruit :"))
match fruit:
  case f if f in ("apple", "banana")  and len(f)>5 :
    print("Fruits Available")
  case _:
    print("Not available")
    
#8
x=str(input("enter the user name :"))
match x:
  case f if f in ("admin") and len(f)>4:
    print("Admin access")
  case f if f in ("user"):
    print("user access")
  case _:
    print("guest access")

    #9
option = int(input("enter the option :"))
match option:
    case 1:
     print("add")
    case 2:
     print("edit")
    case 3:
     print("delete")
    case _:
     print("Invalid option")

 #10
age = int(input("enter the age :"))
match age:
    case age if age > 18:
      print("Eligible for voting")
    case _:
      print("Not eligible")


  
