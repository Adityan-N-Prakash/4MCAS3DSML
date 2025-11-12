import numpy as np
import matplotlib.pyplot as plt

num_languages = int(input("Enter the number of programming languages: "))

x = np.array([input(f"Enter language 1: ")])
y = np.array([float(input(f"Enter the percentage for {x[0]}: "))])

if num_languages > 1:
    x = np.append(x, input(f"Enter language 2: "))
    y = np.append(y, float(input(f"Enter the percentage for {x[1]}: ")))

if num_languages > 2:
    x = np.append(x, input(f"Enter language 3: "))
    y = np.append(y, float(input(f"Enter the percentage for {x[2]}: ")))

if num_languages > 3:
    x = np.append(x, input(f"Enter language 4: "))
    y = np.append(y, float(input(f"Enter the percentage for {x[3]}: ")))

if num_languages > 4:
    x = np.append(x, input(f"Enter language 5: "))
    y = np.append(y, float(input(f"Enter the percentage for {x[4]}: ")))

if num_languages > 5:
    x = np.append(x, input(f"Enter language 6: "))
    y = np.append(y, float(input(f"Enter the percentage for {x[5]}: ")))

plt.pie(y, labels=x)
plt.title('PIE CHART')
plt.show()

