def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index],arr[i] 
    return arr
res=selection_sort([20,12,10,15,2])
print(res)      

def sort(arr):
    n=len(arr)
    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_indx]:
                min_indx=j
        arr[i],arr[min_indx]=arr[min_indx],arr[i]
    return arr
arr=list(map(int,input().split()))
print(sort(arr))               

def min(arr):
    min_index=0
    for i in range(1, len(arr)):
        if arr[i]<arr[min_index]:
            min_index=i
    return arr[min_index]
res=min([8, 4, 6, 2, 9])
print(res)        


def swaps(arr):
    n=len(arr)
    count=0
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        if min_index!=i:
            arr[i],arr[min_index]=arr[min_index],arr[i]
            count+=1
    return count
print(swaps([3,2,1]))

def k_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        
