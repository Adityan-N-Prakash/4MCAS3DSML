import numpy as np
import matplotlib.pyplot as plt

x_input = input("Enter the programming languages (comma-separated): ")
y_input = input("Enter the popularity values (comma-separated): ")

x = np.array(x_input.split(','))
y = np.array([float(i) for i in y_input.split(',')])

plt.bar(x, y)
plt.title('Bar Chart')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')
plt.show()

