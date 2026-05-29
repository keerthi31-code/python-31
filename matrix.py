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

