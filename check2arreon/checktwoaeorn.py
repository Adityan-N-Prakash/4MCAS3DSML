import numpy as np 

input1 = input("Enter the elements for the first array(seperated by spaces): ")
array1 = np.array([x for x in input1.split()])

input2 = input("Enter the elements for the second array(seperated by spaces): ")
array2 = np.array([x for x in input2.split()])

if np.array_equal(array1,array2):
    print("Arrays are equal")
else:
    print("Arrays are not equal.")
