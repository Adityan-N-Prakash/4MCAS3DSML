import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print(f"Enter {rows * cols} elements row-wise:")

elements = []
for _ in range(rows * cols):
    elements.append(float(input()))

arr = np.array(elements).reshape(rows, cols)

print("Original Array:")
print(arr)

arr_transpose = arr.transpose()

print("Transposed Array:")
print(arr_transpose)

