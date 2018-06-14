import matplotlib.pyplot as plt
import numpy as np
points = []
for i in range(100):
    points.append([np.random.randint(100), np.random.randint(100)])
plt.figure('data', figsize = (8, 8))
result = k_means(points, 4)
for kind, point in result:
    if kind == 0:
        plt.plot(point[0], point[1], '.', color = "blue")
    elif kind == 1:
        plt.plot(point[0], point[1], '*', color = "red")
    elif kind == 2:
        plt.plot(point[0], point[1], '.', color = "black")
    elif kind == 3:
        plt.plot(point[0], point[1], '*', color = "green")
plt.show()