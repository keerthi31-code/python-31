#merge 
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

# counting sort practise
def count_sort(arr):
    maximum=max(arr)
    count=[0] * (maximum+1)
    for num in arr:
        count[num]+=1
    j=0
    for i in range(len(count)):
        while count[i]>0:
            arr[j]=i
            j+=1
            count[i]-=1
    return arr
arr=[5,2,4,2,1]
print(count_sort(arr))

def freq(arr):
    maximum=max(arr)
    count=[0] * (maximum + 1)
    for num in arr:
        count[num]+=1
    for i in range(len(count)):
        if count[i]>0:
            print(i, "-->",count[i])

arr=[3,1,2,1,3,2,3]
(freq(arr))


def count_array(arr):
    maximum=max(arr)
    count=[0] * (maximum + 1)
    for num in arr:
        count[num]+=1
    j=0
    for i in range(len(count)):
        if count [i]>0:
            j+=1
    return count
            
arr=[4,1,2,1,4,3]
print(count_array(arr))
print("keerthi")
print("navya")
print("aashritha")
print("manasa")