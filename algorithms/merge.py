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

#######
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half, r_half)
def merge(left, right):
    new=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
arr=[3,5,2,4,9,8] 
print(merge_sort(arr)) 


count=0
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left_arr=merge_sort(left_arr)
    right_arr=merge_sort(right_arr)
    return merge(left_arr, right_arr)
def merge(l,r):
    global count
    count+=1
    array=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            array.append(l[i])
            i+=1
        else:
            array.append(r[j])
            j+=1
    array.extend(l[i:])
    array.extend(r[j:])
    return array
arr=[4,7,3,6,8,5] 
print(merge_sort(arr)) 
print("count:",count)   

def merge_s(arr1,arr2):
    result=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    result.extend(arr1[i:]) 
    result.extend(arr2[j:])
    return result
arr1=[1,3,5]
arr2=[2,4,6] 
print(merge_s(arr1,arr2))  

def mergeSort(left, right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
arr=[4,5,3,2,5,4]
print(merge_sort(arr))


#kth smallest element after sorting
def mergeSort(left, right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return mergeSort(left,right)
arr=[4,5,3,2,9]
k=2
sorted_arr=merge_sort(arr)
print(merge_sort)
print(f"{k}nd smallest element:", sorted_arr[k - 1])

# decending order
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half, r_half)
def merge(left,right):
    dec_arr=[]
    i,j=0,0
    while i <len(left) and j <len(right):
        if left[i]>=right[j]:
            dec_arr.append(left[i])
            i+=1
        else:
            dec_arr.append(right[j])
            j+=1
    dec_arr.extend(left[i:])
    dec_arr.extend(right[j:])
    return dec_arr
arr=[3,4,1,6,2,7]
print(merge_sort(arr)) 

def remove_duplicates(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_half=remove_duplicates(arr[:mid])
    r_half=remove_duplicates(arr[mid:])
    return merge(l_half,r_half)
def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]==right[j]:
            result.append(left[i])
            i+=1
            j+=1
        elif left[i]<right[j]:
            result.append(left[i]) 
            i+=1
        else:
            result.append(right[j])
            j+=1    
    result.extend(left[i:])
    result.extend(right[j:])
    # remove adjacent duplicates
    ans=[]
    for x in result:
        if not ans or ans[-1]!=x:
            ans.append(x)
    return ans
arr=[2,4,3,5,2,5]
print(remove_duplicates(arr))

