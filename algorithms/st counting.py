# arr=[4,2,2,8,3,3]
def counting_sort(arr):
    maximum = max(arr)
    count = [0] * (maximum + 1)   #creating count array

    for num in arr:
        count[num] += 1   #count frequencies

    '''
    count[4]+=1
    [0,0,0,0,1,0,0,0,0]
    count[2]+=1
    [0,0,1,0,1,0,0,0,0]
    finally index:[0,1,2,3,4,5,6,,7,8]
            count:[0 1 2 2 1 0 0 0 1]
    '''

    # prefix sum
    for i in range(1, len(count)):
        count[i] += count[i-1]

    '''
    i=1
    count[1] =1+ (1-1)=0=1
    count[2]=2+1=3...so on
    1 at postiton 1
    2 at position 3..... 8 at position 7
    '''

    output = [0] * len(arr)

    for i in range(len(arr)-1, -1, -1):
        num = arr[i]
        output[count[num]-1] = num
        count[num] -= 1

    return output

arr = [4,2,2,8,3,3,1]
print(counting_sort(arr))
print('keerthi')
print("navya")