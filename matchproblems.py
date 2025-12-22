'''day=int(input("enter the day :"))
match day:
    case 1 if day == 1:
        print("monday")
    case 2 if day ==2:
        print("tuesday")
    case 3 if day == 3:
        print("wednesday")
'''
##2
status = str(input("enter the status :"))
match status.strip():
  case "ok":
    print("success")
  case "error":
   print("failed")
  case _:
   print("unknown status")
    
