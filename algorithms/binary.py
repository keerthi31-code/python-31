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
l=0
r=len(arr)-1
ans=-1
while l<=r:
    m=(l+r)//2
    if arr[m]== t:
        ans=m
        r=m-1
    elif arr[m]<t:
        l=m+1
    else:
        r=m-1
print(ans)                     

def find_target(arr,Target):
    left=0
    right=len(arr)-1
    while left<=right:
        m=(left+right)//2
        if arr[m]==Target:
            return m
        elif arr[m]<Target:
            left=m+1
        else:
            right=m-1
    return -1        
result=find_target([1,2,3,4,5,5],4)
print(result)

