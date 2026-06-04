# arr=list(map(int,input().split()))
# t=int(input())
# for i in range(len(arr)):
#     if arr[i]==t:
#         print("index:",i)


# arr=list(map(int,input().split()))
# k=int(input())
# for i in range(len(arr)):
#     if arr[i]==k:
#         print("index:",i)
   
# arr=list(map(int,input().split()))
# a=int(input())
# for i in range(len(arr)):
#     if arr[i]==a:
#         print(i)

# arr=list(map(int,input().split("," )))
# b=int(input("Target:"))
# count=0
# for num in arr:
#     if num >1:
#         count+=1
# print(count) 


arr=[4,7,2,9,1]
num=0 #num = 0
for i in arr: #i=4,7,2,9,1
    if i > num: #4>0 ,7>4 -- true ,9>7 true,4>2, i=1 1>9 no -- no 
        num=i # num 4 
                # num=7
                # num=7
                #num=9
                #num remains same num=9

print("largestno.",num)

lst=[4,7,2,9,1]
num=lst[0]
for i in lst:
    if i < num:
        num=i
print(num)   



lst=[1,2,3,4,5,6]
num=int(input())
found=False
for i in lst:
    if i==num:
        found = True

if found:
    print("yes")
else:
    print("no")             
