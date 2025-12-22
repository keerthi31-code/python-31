'''day=int(input("enter the day :"))
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

grade = str(input("enter the grade :"))
match grade:
 case "A"|"B":
  print("Good performance")
 case"C":
  print("Average performance")
 case _:
  print("Invalid grade")
'''
choice = int(input("enter the value :"))
match choice:
  case 1:
   print("Start")
  case 2:
   print("Stop")
    
