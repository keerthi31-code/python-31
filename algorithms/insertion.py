def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=insertion_sort([5,4,2,1,6,3])
print(arr) 


def sort_insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key =arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=sort_insertion([3,5,76,9,2,1])
print(arr)        


def count_shifts(arr):
    n=len(arr)
    count=0
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            count+=1
            j-=1
        arr[j+1]=key
    return count
arr=count_shifts([5,4,3])
print(arr) 


def des_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]< key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=des_sort([5,2,8,1])
print(arr)   


def insert_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]> key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print(f"pass{i}:{arr}")
    return arr
insert_sort([9,1,5,3,2])        

def count_passes(arr):
    n = len(arr)
    passes = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        passes += 1
    return passes
print(count_passes([9, 1, 5, 3, 2]))

def sorted(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
        return True
arr=[1,2,3,4,5] 
if sorted(arr):
    print("already sorted")
else:
    print("not sorted")       

def k_sort(arr,k):
    n= len(arr)
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if i ==k:
            return arr
    return arr    
arr=[1,5,3,7,8,4]
k=2
print(k_sort(arr, k))

def sort_insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key    
    return arr

arr=list(map(int,input().split()))
print(sort_insertion(arr))


def sort_steps(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        print (f"(pass{i}:{arr})")
    return arr
arr=list(map(int,input().split()))
print(sort_steps(arr))

def count_shifts(arr):
    n=len(arr)
    shifts=0
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            shifts+=1 # inside while loop it count shifts outside count passes
            j-=1
        arr[j+1]=key
        
    return shifts
arr=list(map(int,input().split()))
print(count_shifts(arr))
