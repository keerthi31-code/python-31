# #1
# age=int(input("enter your age:"))
# if age>21:
#     print(True)
# else:
#     print(False)
#2
# marks=int(input("enter the marks:"))
# if marks==50:
#     print("pass")
# elif marks>50:
#     print("passed")
# else:
#     print("failed")

#3
# num=int(input("enter the number:"))
# if num%5==0:
#         print(True)
# else:
#         print(False)

#4
# def replace_smiley(text):
#   return text.replace(":)", "😊")

# input_text="Hello :) How are you :) ?"
# result=replace_smiley(input_text)
# print(result)

# input_text="hi :) how is your day :) ?"
# result=replace_smiley(input_text)
# print(result)

#9
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
# for num in numbers:
#  if num%2==0:
#    continue
#  print(num)

correct_password="keerthi12345"
while True:
    
  x=input("enter the passwords:")
  if x==correct_password:
      print("success message")
      break
  else:
      print("wrong try again")

while True:
  x=int(input("enter the value: "))
  if x>0:
   print("you entered the positive value")
   break
  print("stops! you entered negative value")


