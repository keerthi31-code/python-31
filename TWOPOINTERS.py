
'''
Two pointers technique uses 2 indices to solve problems on arrays or strings 
instead of nested loops O(n^2) , it solves problems in O(n)
starts from opposite side 
starts from the same side
moves at different speed (slow and fast pointers)

'''
# type 1 opposite ends
arr=[1,2,3,4,6,8,10]
target=10
left=0
right=len(arr)-1

while left<right:
    s=arr[left]+arr[right]
    
    if s==target:
        print(arr[left],arr[right])
        break
    elif s<target:
        left+=1
    else:
        right-=1

# type 2- same direction 
nums=[0,1,0,3,12]
slow=0
for fast in range(len(nums)):
    if nums[fast]!=0:
        nums[slow],nums[fast]=nums[fast],nums[slow]
        slow+=1
print(nums)
#slow moves 1 step
#fast moves 2  steps

def palindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            print(False)
            break
        l+=1
        r-=1
    else:
        print(True)

'''

Reverse an array using two pointers.
Check if a string is a palindrome.
Find two numbers in a sorted array with a given sum.
Move all zeros to the end.
Remove duplicates from a sorted array.
Merge two sorted arrays.
Sort colors (Dutch National Flag problem).
Container With Most Water (LeetCode 11).
3Sum (LeetCode 15).
Trapping Rain Water (LeetCode 42).
'''

def rev_arr(arr):
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
arr=[10,20,30,40,50]
print(rev_arr(arr))


s='momi'
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print(False)
        break
    else:
        left+=1
        right-=1
    print(True)

def two_sum(arr, target):
    current_sum=0
    l=0
    right=len(arr)-1
    while l<right:
        current_sum=arr[l]+arr[right]

        if current_sum==target:
            return [l,right]
        elif current_sum>target:
            right-=1
        else:
            l+1
    return []
arr=[2,4,6,8,10]
target=6
print(two_sum(arr,target))

def move_zeroes(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[pos]=arr[pos],arr[i]
            pos+=1
    return arr
arr=[1,0,3,0,5,6]
print(move_zeroes(arr))

def remove_duplicates(arr):
    res=[]
    left=0
    right=len(arr)-1
    while left<right:
        s=arr[left],arr[right]
    if arr[left]!=arr[right]:
        res.append(s)
    else:
        left+=1
        right-=1
arr=[1,2,1,4,5,6,6,7,8]
print(remove_duplicates(arr))



def prime_num(n):
    for i in n:
        if i%2==0:
            return False
        else:
            return n
print(prime_num(30))
        