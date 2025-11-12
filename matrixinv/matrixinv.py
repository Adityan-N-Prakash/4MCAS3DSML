import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print(f"Enter the elements for a {rows}x{cols} matrix:")
matrix_elements = [list(map(float, input(f"Enter row {i + 1} elements (space-separated): ").split())) for i in range(rows)]

m = np.array(matrix_elements)

print("Original matrix:")
print(m)

det = np.linalg.det(m)

if det != 0:
    result = np.linalg.inv(m)
    print("Inverse of the matrix:")
    print(result)
else:
    print("The matrix is singular and cannot be inverted.")

