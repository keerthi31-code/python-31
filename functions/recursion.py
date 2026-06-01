#recursion is when function calls itself
def print_numbers(n):
    if n==0:
        return
    print(n)
    print_numbers(n-1)
print_numbers(5)    

def printnumbers(n):
    if n==0:
        return
    print(n)
    printnumbers(n-1)
printnumbers(3) 

def sumNums(n):
    if n==1:
        return 1
    sum=n+sumNums(n-1)
    return sum
print(sumNums(4))  


# in dfs when ever there is a row col(2[row],3[col])
'''
up down right left co ordinates are depends
up -- row-1 (1,3)  -- (r-1,c)
down -- row+1 (3,3) --(r+1,c)
right-- col+1 (2,4)--(r,c+1)
left-- col-1 (2,2)--(r,c-1)



When DFS reaches (r, c):
1. Is (r, c) inside the grid?
   No → Stop
2. Does this cell have the original color?
   No → Stop
3. Color this cell.
4. Visit:
   Up
   Down
   Left
   Right



1 1 1
1 1 0
1 0 1

(0,0) (0,1) (0,2)
  1     1     1

(1,0) (1,1) (1,2)
  1     1     0

(2,0) (2,1) (2,2)
  1     0     1

lets start with r,c (1,1)
using 
up=(r-1,c)=0,1=1
down=(r+1,c)=2,1=0
left=(r,c-1)=1,0=1
ryt=(r,c+1)=1,2=0

'''