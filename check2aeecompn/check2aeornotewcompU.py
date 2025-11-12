import numpy as np 

arr1 = np.array(list(map(int, input("Enter first array elements: ").split())))
arr2 = np.array(list(map(int, input("Enter second array elements: ").split())))

print("First array: ", arr1)
print("Second array: ", arr2)

comp = arr1 == arr2
print(comp)

