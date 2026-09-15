# Addition of two matrices

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter elements of second matrix:")
B = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

# Matrix addition
C = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Sum of the two matrices:")

for row in C:
    print(row)
