n=int(input("enter the value: "))
if n & 1:
    print("odd")
else: 
    print("even")  

for i in range(1,6):
    if i &1:
        print(i,"odd") 
    else:
        print(i, "even")   

lst=[2,3,2,4,4]
result =0
for i in lst:
    result=result^i
print(result)        