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

