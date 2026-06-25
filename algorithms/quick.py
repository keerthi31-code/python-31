'''
QuickSort(arr):
    if array has 0 or 1 element:
        return

    Choose a pivot
    Partition array around pivot

    QuickSort(left part)
    QuickSort(right part)
'''


def quick_sort(arr):
    n = len(arr)
    if n<=1:
        return arr

    pivot = arr[n//2]
    left = []
    middle=[]
    right = []
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)

        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right) 
            
a = [8,6,4,9,1,2]
print(quick_sort(a))


def sort_quick(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[n//2]
    left =[]
    middle=[]
    right=[]
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x>pivot:
            right.append(x)
        else:
            middle.append(x)
    return sort_quick(left)+middle+sort_quick(right)
arr=[6,4,3,7,5,2,1]
print(quick_sort(arr))


