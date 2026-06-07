# arr=list(map(int,input().split()))
# t=int(input("enter the value:"))
# l=0
# r=len(arr)-1
# while l<=r:
#     m=l+r//2
#     if arr[m]==t:
#         print(m)
#         break
#     elif arr[m]<t:
#         l=m+1  
#     else:
#         r=m-1      


arr=[2,4,6,8,10,12]
t=int(input("Target:")) 
l=0
r=len(arr)-1
while l<=r:
    m=(l+r)//2
    if arr[m]==t:
        print(m)
        break
    elif arr[m]<t:
        l=m+1
    else:
        r=m-1    


arr=[1,2,5,6,7,4] 
t=int(input("target:"))
for i in range(len(arr)-1):
    if i in arr:
        t==i
    print("yes")
    break 
else:
    print("no")          


