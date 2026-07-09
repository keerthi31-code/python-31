def counting_sort(arr):
    maximum = max(arr)
    count = [0] * (maximum + 1)
    # Count frequencies
    for num in arr:
        count[num] += 1
    # Build sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr)) 

def counting_sort(arr): # arr = [4,2,2,8,3,3,1] 
    maximum=max(arr) #  8
    count=[0] * (maximum+1) #[0 0 0 0 0 0 0 0]
    # count frequency
    for num in arr:
        count[num]+=1
    j=0
    for i in range(len(count)):
        while count[i]>0:
            arr[j]=i
            j+=1
            count[i]-=1
    return arr
a=[4, 2, 2, 8, 3, 3, 1]
print(counting_sort(a))

# stable counting
def counting_sort(arr): # arr = [4,2,2,8,3,3,1] 
    maximum=max(arr) #  8
    count=[0] * (maximum+1) #[0 0 0 0 0 0 0 0]
    for num in arr:
        count[num]+=1
    #cummulative count
    for i in range(1, len(count)):
        count[i]+=count[i-1]
    output =[0]*len(arr)
    for j in reversed(arr):
        output[count[j]-1]=j
        count[j]-=1
    return output
a=[4, 2, 8, 3, 3, 1]
print(counting_sort(a))


