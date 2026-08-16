'''
1. Minimum Sum
Problem: You are given two integer arrays A and B of length N on
which you have to perform below operation:
In one operation, you can swap any two elements of 'A' or any two 
elements of 'B'Consulting

Your task is to find and return an integer value 
representing the minimum possible sum of A[i]*B[i]
after performing the above operation any number of times.
Note: The operation can also be performed 0 number of times.

Input Specification:

input1: An integer value N representing the size of arrays.
input2: An integer array A
input3: An integer array B
Output Specification: Return an integer value representing 
the minimum possible sum of A[i]*B[i] after performing 
the above operation any number of times.

Example 1:

input1: 4
input2: {1,4,1,6}
input3: {1,4,3,4}
Output: 25
Programming
Explanation: Here A = {1,4,3,2} and B = {1,4,3,4}.
To minimize the sum, we can swap the first two elements of A i.e., 4 and 1.
The array will now become (4,1,3,2). The sum obtained will be 25,
which is the minimum.
Hence, 25 is returned as the output.
input1: 3
input2: (4,1,6)
input3: (3,1,2)
Output: 17

input1: 3
input2: 2
input3: {{2, 4}, {0, 0}, {11, 11}}
Output: 1
Computer Science
Explanation: Here, the given 2D given array {{2, 4}, {0, 0}, {11, 11}}, Only the last row {11, 11}
has odd elements and their sum is 22 which is even. Therefore, there is only 1 magical row so, 1 is returned as the output
'''
def sum_arrs(arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)
    result=0
    for i in range(len(arr1)):
        result+=arr1[i]*arr2[i]
    return result
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(sum_arrs(arr1,arr2))
'''
Alex has a list of books with reading times in array A, 
and N hours available. Determine the maximum number 
of books he can read without exceeding his available hours. 
INPUT / OUTPUT 
input1: array A of reading times. 
input2: N hours available. 
input3: size of A. Output: max books.
EXAMPLE input1: [4,2,3,1] 
input2: 5 
input3: 4 
Output: 2
'''
# Knowledge Enhancement
def max_books(arr,n,l):
    for i in range(len(arr)):
        if i<=n:
            i+=1
            break
    return (n)
arr=list(map(int, input().split()))
n=int(input())
l=int(input())
print(max_books(arr,n,l))

'''
Given an array of integers and an integer n, 
find the sum of the n largest unique elements, 
then subtract the largest of those n elements (a discount). 
Return the result. 
If n is greater than the number of unique elements, return 0. 
INPUT / OUTPUT Input: arr (list), n (count). Output: discounted sum. 
Constraint: 1 ≤ n ≤ len(arr). EXAMPLE Input: arr=[5,2,9,1,7,4,6], n=3 
Output: 13   (9+7+6=22, minus 9) 
Input: arr=[5,2,9,1,7,4,6], n=1 Output: 0    
(9 minus 9)
'''

def n_largest(arr,n):
    
    for i in range(len(arr),n):
        sum1+=i
        break
        sum1=sum1-max(arr)
    return sum1
arr=[5,2,9,1,7,4,6]
n=3
print(n_largest(arr,n))
print("keerthi")
