import numpy as np
import matplotlib.pyplot as plt

x_input = input("Enter the values for x-axis (comma-separated): ")
y_input = input("Enter the values for y-axis (comma-separated): ")

x = np.array([float(i) for i in x_input.split(',')])
y = np.array([float(i) for i in y_input.split(',')])

plt.plot(x, y, color='red', marker='o', mfc='green', mec='black', linestyle='dotted')
plt.title('Line Diagram')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

