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

arr=list(map(int,input().split("," )))
b=int(input("Target:"))
count=0
for num in arr:
    if num >1:
        count+=1
print(count)    