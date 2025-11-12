import numpy as np

a = float(input())
b = float(input())
c = float(input())
d = float(input())

m = np.array([[a, b], [c, d]])

print("Original matrix:")
print(m)

try:
    result = np.linalg.inv(m)
    print("Inverse of the said matrix:")
    print(result)
except np.linalg.LinAlgError:
    print("The matrix is singular and cannot be inverted.")

