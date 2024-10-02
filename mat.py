matrix = [
    [1, 2],
    [4, 5]
]
print("ORIGINAL MADTRIX:")
print(".........................")
for row in matrix:
    print(row)

op=int(input("Enter \n 1 for rotate matrix in clockwise\n 2 for rotate matrix in anticlockwise \n enter your choice :  "))
if op==1:
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
    print("\nRotated Clockwise:")
    print("..........................")
    
    for row in matrix:
        print(row)

if op==2:
    n=len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
    print("\nRotated Anticlockwise:")
    print(".......................................")
    for row in matrix:
        print(row)

