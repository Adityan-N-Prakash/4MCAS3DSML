import numpy as np
import matplotlib.pyplot as plt

x_input = input("Enter the values for x1-axis (comma-separated): ")
y_input = input("Enter the values for y1-axis (comma-separated): ")
x1_input = input("Enter the values for x2-axis (comma-separated): ")
y1_input = input("Enter the values for y2-axis (comma-separated): ")

x = np.array([float(i) for i in x_input.split(',')])
y = np.array([float(i) for i in y_input.split(',')])
x1 = np.array([float(i) for i in x1_input.split(',')])
y1 = np.array([float(i) for i in y1_input.split(',')])

plt.plot(x, y, color='red', marker='o', mfc='blue', mec='black')
plt.plot(x1, y1, color='blue', marker='o', mfc='red', mec='black')
plt.title('Legend Diagram')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(['Red', 'Blue'])
plt.show()

