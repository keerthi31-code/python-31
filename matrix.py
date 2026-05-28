rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row by row:")

for i in range(rows):
    
    row = list(map(int, input().split()))
    
    while len(row) != cols:
        print(f"Please enter exactly {cols} elements.")
        row = list(map(int, input().split()))
    
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Transpose
transpose = []

for col in range(cols):
    
    temp = []
    
    for row in range(rows):
        temp.append(matrix[row][col])
    
    transpose.append(temp)

print("\nTranspose Matrix:")
for row in transpose:
    print(row)