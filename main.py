import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist


X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

z = np.array([[5, 1], [2, 2]])
distance = np.zeros(len(X))

file0 = open("file0.txt", "w")
file1 = open("file1.txt", "w")

for i in range(len(X)):
    distance = np.zeros(len(z))
    for iz, zi in enumerate(z, 0):
        distance[iz] = np.sqrt(((X[i][0]-zi[0])+(X[i][1]-zi[1]))**2)
    min_idx = np.argmin(distance)
    if min_idx == 0:
        file0.write(str(X[i][0])+" "+str(X[i][0])+"\n")
    else:
        file1.write(str(X[i][0]) + " " + str(X[i][0]) + "\n")

"""
distances = cdist[X, centers]
closest = np.argmin(distances, axis=1)
X[closest == 0].mean[axis = 0]
for i in range(k):
    centers[i, :] = X[closest == i].mean(axis=0)
centers
np.random.seed(4160659)
X[closest == 0].mean(axis=0)
closest = np.zeros(n).astype(int)
for interation in range(3)
    print(closest)
distances = cdist(x, centers)
closest = np.argmin(distances, axis=1)

for i in range(k):
    centers[i, :] = X[closest == i].mean(axis=0)

plt.scatter(X[:, 0], X[:, 1], c=closest)
"""