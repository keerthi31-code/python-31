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
def replace_smiley(text):
  return text.replace(":)", "😊")

input_text="Hello :) How are you :) ?"
result=replace_smiley(input_text)
print(result)
