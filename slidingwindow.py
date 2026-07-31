
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


s='abababd'
p='ab'
k=len(p)
count=0
for ch in range(len(s)-k+1):
    if s[ch:ch+k]==p:
        count+=1
print(count)



from collections import deque
def slide_window_max(nums,k):
    dq=deque()
    result=[]
    n=len(nums)
    for i in range(n):
        while dq and dq[0]<=i:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop
        dq.append(i)

        if i>=k-1:
            result.append(nums[dq[0]])
    return result
nums=list(map(int, input().split()))
k=int(input())
print(slide_window_max(nums,k))