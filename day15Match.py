#match 
'''
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    

    #default value

day = 4
match day:
  case 6:
   print("saturday")
 
  case 7:
   print("sunday")

  case _:
   print("Looking forward to next week")
  
# combine values in it we pipe | character for combining the values under a case
day = 3
match day:
    case 1 | 2| 3| 4| 5:
        print("these are week days")
    case 6|7:
        print("i love weekends")
        '''
# if stmt as guard
month = 3
day = 7
match day:
 case 1|2|3|4|5 if month == 4:
  print("week day in april")
 case 1|2|3|4|5 if month == 5:
  print("week day in may")
 case 1|2|3|4|5 if month ==3:
  print("week day march")
 case _:
  print("not match")
  
  #


      