import numpy as np

n = int(input("Enter the size of the square matrix (n): "))

matrix = []
for i in range(n):
    row = input(f"Enter row {i+1} values separated by spaces: ").split()
    row = [int(x) for x in row]
    while len(row) != n:
        print(f"Please enter exactly {n} values.")
        row = input(f"Enter row {i+1} values separated by spaces: ").split()
        row = [int(x) for x in row]
    matrix.append(row)

matrix = np.array(matrix)

print("The matrix is:")
print(matrix)

trace_value = np.trace(matrix)
print(f"The trace of the matrix is: {trace_value}")

