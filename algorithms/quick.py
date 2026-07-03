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

def partition(arr, low, high):
    pivot = arr[high]      # Last element as pivot
    i = low - 1
    swaps = 0
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            if i != j:      # Count only actual swaps
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    if i + 1 != high:       # Place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
    return i + 1, swaps

def quick_sort(arr, low, high):
    swaps = 0
    if low < high:
        pivot_index, count = partition(arr, low, high)
        swaps += count
        swaps += quick_sort(arr, low, pivot_index - 1)
        swaps += quick_sort(arr, pivot_index + 1, high)
    return swaps
arr = [6, 4, 3, 7, 5, 2, 1]
total_swaps = quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
print("Total Swaps:", total_swaps)


