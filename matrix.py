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

a=[]
b=[]
rows=int(input("enter rows: "))
cols=int(input("eneter cols: "))
print("enter matrix A: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    a.append(row)    
print(a)
print("enetr matrix B: ")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    b.append(row)
print(b)
c=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(a[i][j]+b[i][j])
    c.append(row)
print("Result: ")
for row in c:
    print(row)        


#subtraction
a=[]
b=[]
rows=int(input("enter rows:"))
cols=int(input("enter cols:"))
print("enter matrix A:")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    a.append(row)  

print("enter matrix B:")
for i in range(rows):
    for j in range(cols):
        row.append(int(input()))
    b.append(row) 

c=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(a[i][j]-b[i][j])
    c.append(row)
print(c)    






