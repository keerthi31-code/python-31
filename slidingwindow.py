
def sliding_window(nums, k):
    # Step 1-Calculate first window
    window_sum = sum(nums[:k])

    answer = window_sum

    # Step 2- Slide the window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        answer = max(answer, window_sum)

    return answer
k=3
nums=[2,1,5,1,3,2]
print(sliding_window(nums,k))