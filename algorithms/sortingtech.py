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