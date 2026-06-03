arr=list(map(int,input().split()))
t=int(input("enter the value:"))
l=0
r=len(arr)-1
while l<=r:
    m=l+r//2
    if arr[m]==t:
        print(m)
        break
    elif arr[m]<t:
        l=m+1  
    else:
        r=m-1      