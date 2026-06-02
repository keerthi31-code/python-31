#add
a = [[1,2],
    [3,4]] 
b = [[5,6],
    [7,8]]
total=[0,0],[0,0]
rows=2
cols=2
for i in range(rows):
    for j in range(cols):
        total[i][j]=a[i][j]+b[i][j]
    print(total)    
#sub---------------------------------
a1=[2,3,4],[5,6,8],[10,11,12]
b1=[2,3,4],[5,6,8],[10,11,12]
res=[0,0,0],[0,0,0],[0,0,0]
row=3
col=3
for i in range(row):
    for j in range(col):
        res[i][j]=a1[i][j]-b1[i][j]
print(res)
#mul-----------------------------------
a=[[1,2,3],
   [2,3,4],
   [3,4,5]]

b=[[1,2],
   [2,3],
   [3,4]]

result=[]
for i in range(len(a)):          # here len(a) is an row                                   
    row=[0]*len(b[0])            # here len(b[0])  is no of colums -->  if confuse refer matrix-1.py
    for j in range(len(b[0])):      
        for k in range(len(b)):
            row[j]+=a[i][k]*b[k][j]
    result.append(row)
print(result)   


# Practise

a=[1,2],[3,4]
b=[5,6],[7,8]
c=[0,0],[0,0]
row=2
col=2
for i in range(row):
    for j in range(col):
        c[i][j]=a[i][j]+b[i][j]
print(c) 

a=[1,2,3],[4,5,6],[7,8,9]
b=[9,8,7],[6,5,4],[3,2,1]
c=[0,0,0],[0,0,0],[0,0,0]
rows=3
cols=3
for i in range(rows):
    for j in range(cols):
        c[i][j]=a[i][j]+b[i][j]
for i in c:
    print(i)

# a=[]
# b=[]
# rows=int(input("enter rows: "))
# cols=int(input("eneter cols: "))
# print("enter matrix A: ")
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input()))
#     a.append(row)    
# print(a)
# print("enetr matrix B: ")
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input()))
#     b.append(row)
# print(b)
# c=[]
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(a[i][j]+b[i][j])
#     c.append(row)
# print("Result: ")
# for row in c:
#     print(row)        


# #subtraction
# a=[]
# b=[]
# rows=int(input("enter rows:"))
# cols=int(input("enter cols:"))
# print("enter matrix A:")
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input()))
#     a.append(row)  

# print("enter matrix B:")
# for i in range(rows):
#     for j in range(cols):
#         row.append(int(input()))
#     b.append(row) 

# c=[]
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(a[i][j]-b[i][j])
#     c.append(row)
# print(c)    


a=[1,2],[4,5]
b=[3,4],[8,7]
c=[0,0],[0,0]
rows=2
cols=2
total=0
for i in range(rows):
    for j in range(cols):
        c[i][j]=a[i][j]+b[i][j]
        total+=c[i][j]
print("matix:")
for row in c:
    print(row)        
print(total)        


a=[[1,2,3], #a[0]=123, #a[0][1]= 2
   [2,3,4]]
b=[[4,5,6],
   [8,9,6]]
c=[[0,0,0],
   [0,0,0]]
rows=2
cols=3
for i in range(rows):
    for j in range(cols):
        c[i][j]=a[i][j]
for row in c:        
    print(row)

'''
1. Variables, Input/Output, Basic Math
    1. Palindrome Number — LeetCode #9
    2. Plus One — LeetCode #66
    3. Add Digits — LeetCode #258
    4. Subtract the Product and Sum of Digits of an Integer — LeetCode #1281
    5. Maximum 69 Number — LeetCode #1323

2. Conditional Statements (if-else)
    1. Fizz Buzz — LeetCode #412
    2. Power of Two — LeetCode #231
    3. Valid Perfect Square — LeetCode #367
    4. Ugly Number — LeetCode #263
    5. Toeplitz Matrix — LeetCode #766

3. Loops (for, while)
    1. Climbing Stairs — LeetCode #70
    2. Count Odd Numbers in an Interval Range — LeetCode #1523
    3. Number of Steps to Reduce a Number to Zero — LeetCode #1342
    4. Find Numbers with Even Number of Digits — LeetCode #1295
    5. Self Dividing Numbers — LeetCode #728

4. Strings
    1. Valid Anagram — LeetCode #242
    2. Reverse String — LeetCode #344
    3. Longest Common Prefix — LeetCode #14
    4. Valid Palindrome — LeetCode #125
    5. Roman to Integer — LeetCode #13

5. Lists / Arrays
    1. Two Sum — LeetCode #1
    2. Best Time to Buy and Sell Stock — LeetCode #121
    3. Contains Duplicate — LeetCode #217
    4. Move Zeroes — LeetCode #283
    5. Maximum Subarray — LeetCode #53

6. List Comprehension / Nested Lists
    1. Transpose Matrix — LeetCode #867
    2. Matrix Diagonal Sum — LeetCode #1572
    3. Reshape the Matrix — LeetCode #566
    4. Flipping an Image — LeetCode #832
    5. Lucky Numbers in a Matrix — LeetCode #1380

7. Functions
    1. Search Insert Position — LeetCode #35
    2. Sqrt(x) — LeetCode #69
    3. Missing Number — LeetCode #268
    4. Find Pivot Index — LeetCode #724
    5. Majority Element — LeetCode #169

8. Recursion
    1. Fibonacci Number — LeetCode #509
    2. Power of Three — LeetCode #326
    3. Binary Search — LeetCode #704
    4. Merge Two Sorted Lists — LeetCode #21
    5. Maximum Depth of Binary Tree — LeetCode #104

9. Dictionaries / HashMaps
    1. Intersection of Two Arrays — LeetCode #349
    2. Jewels and Stones — LeetCode #771
    3. First Unique Character in a String — LeetCode #387
    4. Find the Difference — LeetCode #389
    5. Word Pattern — LeetCode #290

10. Sets & Tuples
    1. Single Number — LeetCode #136
    2. Happy Number — LeetCode #202
    3. Contains Duplicate II — LeetCode #219
    4. Intersection of Two Arrays II — LeetCode #350
    5. Unique Number of Occurrences — LeetCode #1207

11. Sorting
1. Sort Array By Parity — LeetCode #905
2. Height Checker — LeetCode #1051
3. Relative Sort Array — LeetCode #1122
4. Squares of a Sorted Array — LeetCode #977
5. Third Maximum Number — LeetCode #414

12. Searching (Linear & Binary Search)
1. Binary Search — LeetCode #704
2. Guess Number Higher or Lower — LeetCode #374
3. First Bad Version — LeetCode #278
4. Peak Index in a Mountain Array — LeetCode #852
5. Search in Rotated Sorted Array — LeetCode #33

13. Stack & Queue Basics
1. Valid Parentheses — LeetCode #20
2. Implement Queue using Stacks — LeetCode #232
3. Baseball Game — LeetCode #682
4. Backspace String Compare — LeetCode #844
5. Min Stack — LeetCode #155

14. File Handling Style Problems (String Parsing)
1. Length of Last Word — LeetCode #58
2. Count Binary Substrings — LeetCode #696
3. Detect Capital — LeetCode #520
4. Goal Parser Interpretation — LeetCode #1678
5. Truncate Sentence — LeetCode #1816

15. OOPs Concepts
Classes & Objects
1. Design Parking System — LeetCode #1603
2. Design HashSet — LeetCode #705
3. Design HashMap — LeetCode #706
4. Design Browser History — LeetCode #1472
5. Shuffle an Array — LeetCode #384

Inheritance / Polymorphism / Design Based
1. Employee Importance — LeetCode #690
2. Peeking Iterator — LeetCode #284
3. Iterator for Combination — LeetCode #1286
4. Design Circular Queue — LeetCode #622
5. LRU Cache — LeetCode #146
'''
x=int(input())
s=str(x)
rev=s[::-1]
if s==rev:
    print(True)
else:
    print(False)    
