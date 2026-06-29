def merge_sort(arr):# [8,6,4,9,1,2]
    n = len(arr)
    l = 0
    r = n-1
    if n>1:
        mid = (l+r)//2 
        left = arr[:mid+1]
        right = arr[mid+1:]
        #print("before:",left, right)
        merge_sort(left)
        merge_sort(right)
        #print("after", left, right)
        i=j=k=0
        while i< len(left) and j < len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i< len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr 
a = [8,6,4,9,1,2]
print(merge_sort(a))

def mergeSort(arr):
    n=len(arr)
    l=0
    r=n-1
    if n>1:
        mid=(l+r)//2
        left=arr[:mid+1]
        right=arr[mid+1:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr
arr=[4,6,2,3,1,8,9]
print(mergeSort(arr))

count = 0

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    global count

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    count += 1          # Count every merge
    return merge(left, right)


arr = [38, 27, 43, 3]

sorted_arr = merge_sort(arr)

print("Sorted Array:", sorted_arr)
print("Merge Operations:", count)
