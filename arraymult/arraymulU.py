import numpy 

arr1_input = input("Enter the elements for the first array (comma-separated): ")
arr2_input = input("Enter the elements for the second array (comma-separated): ")

arr1 = list(map(int, arr1_input.split(',')))
arr2 = list(map(int, arr2_input.split(',')))

print("1st Input array : ", arr1)
print("2nd Input array : ", arr2)

out_num = numpy.multiply(arr1, arr2)
print("Output values after multiplication : ", out_num)

