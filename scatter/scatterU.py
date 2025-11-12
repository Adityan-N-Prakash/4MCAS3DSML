import numpy as np
import matplotlib.pyplot as plt

num_students = int(input("Enter the number of students: "))

maths = np.zeros(num_students)
science = np.zeros(num_students)

i = 0
maths[i] = float(input(f"Enter marks for Maths (Student {i+1}): "))
science[i] = float(input(f"Enter marks for Science (Student {i+1}): "))

i = 1
if num_students > 1:
    maths[i] = float(input(f"Enter marks for Maths (Student {i+1}): "))
    science[i] = float(input(f"Enter marks for Science (Student {i+1}): "))

i = 2
if num_students > 2:
    maths[i] = float(input(f"Enter marks for Maths (Student {i+1}): "))
    science[i] = float(input(f"Enter marks for Science (Student {i+1}): "))

plt.scatter(maths, science, color='blue', marker='o')
plt.title("SCATTERPLOT")
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")
plt.grid()
plt.show()

