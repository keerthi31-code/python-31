#BUBBLE SORT
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):#6
#         for j in range(0, n-i-1):#6-1-1=4
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
    
# arr=[5, 3, 8, 1, 2]
# result=bubble_sort(arr)   
# print(result)

def sorting_ele(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr
arr=[7,5,3,8,1]
result=sorting_ele(arr)
print(result)            


def sort_des(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[7,2,9,1]
result=sort_des(arr)
print(result) 

# count swaps
def sort_count(arr):
    n=len(arr)
    count=0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
    return count
arr=[4,3,2,1] 
result=sort_count(arr)
print(result)   

def sorted_array(arr):
    n=len(arr) 
    for i in range(n-1):
            if arr[i]>arr[i+1]:
                return "not sorted"
    return "sorted"
arr=list(map(int,input().split()))
print(sorted_array(arr))    

def largest_ele(arr):
    n=len(arr)
    for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr[-1]
arr=[5,1,8,3]
print(largest_ele(arr))

