##Variable sliding window ---------
# nums = [2,3,1,2,4,3]
def longest_subarr(nums, k):

    left =0
    
    max_len = 0
    total=0

    for right in range(len(nums)):
        total += nums[right]
        #print(total)

        while total>k:
            total-=nums[left]

            left+=1
            #best subarray
            if right-left+1 > max_len:
                max_len = right-left+1

                st = left
                en = right

    return nums[st:en+1], max_len
arr = [2,3,1,2,4,3]
n=7
print(longest_subarr(arr,n))