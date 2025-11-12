import numpy as np
import matplotlib.pyplot as plt

num_languages = int(input("Enter the number of programming languages: "))

x = np.array([input("Enter language 1: ")])
y = np.array([float(input(f"Enter the popularity percentage for {x[0]}: "))])

if num_languages > 1:
    x = np.append(x, input("Enter language 2: "))
    y = np.append(y, float(input(f"Enter the popularity percentage for {x[1]}: ")))

if num_languages > 2:
    x = np.append(x, input("Enter language 3: "))
    y = np.append(y, float(input(f"Enter the popularity percentage for {x[2]}: ")))

if num_languages > 3:
    x = np.append(x, input("Enter language 4: "))
    y = np.append(y, float(input(f"Enter the popularity percentage for {x[3]}: ")))

if num_languages > 4:
    x = np.append(x, input("Enter language 5: "))
    y = np.append(y, float(input(f"Enter the popularity percentage for {x[4]}: ")))

if num_languages > 5:
    x = np.append(x, input("Enter language 6: "))
    y = np.append(y, float(input(f"Enter the popularity percentage for {x[5]}: ")))

colors = []
colors.append(input(f"Enter color for {x[0]} bar: "))
if num_languages > 1:
    colors.append(input(f"Enter color for {x[1]} bar: "))
if num_languages > 2:
    colors.append(input(f"Enter color for {x[2]} bar: "))
if num_languages > 3:
    colors.append(input(f"Enter color for {x[3]} bar: "))
if num_languages > 4:
    colors.append(input(f"Enter color for {x[4]} bar: "))
if num_languages > 5:
    colors.append(input(f"Enter color for {x[5]} bar: "))

plt.barh(x, y, color=colors)
plt.title('Horizontal Bar Chart')
plt.xlabel('Programming Language')
plt.ylabel('Popularity')
plt.show()

