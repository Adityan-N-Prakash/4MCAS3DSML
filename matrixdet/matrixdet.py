import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print(f"Enter the elements for a {rows}x{cols} matrix:")

matrix_elements = input(f"Enter {rows * cols} elements (space-separated): ").split()

m = np.array(matrix_elements, dtype=float).reshape(rows, cols)

print("The matrix is:")
print(m)

det = np.linalg.det(m)

print(f"The determinant of the matrix is: {det}")

