import numpy as np
import matplotlib.pyplot as plt
import math


def new_centroid_axis(x):
    c = 0
    for i in x:
        c += i
    return c/(len(x))


dataA = np.array([[i for i in  np.random.normal(0.3, 0.06, 500)], [i for i in np.random.normal(0.48, 0.02, 500)]])
dataB = np.array([[i for i in np.random.normal(0.7, 0.05, 520)], [i for i in np.random.normal(0.5, 0.03, 520)]])

data = np.concatenate((dataA , dataB), axis=1)

BaseA = []
BaseB = []

range_to_point = lambda c, x: math.sqrt((c[0] - x[0])**2 + (c[1] - x[1])**2)

CentroidA = np.array([np.random.uniform(0.1, 0.5), np.random.uniform(0.3, 0.6)])
CentroidB = np.array([np.random.uniform(0.55, 0.8), np.random.uniform(0.4, 0.66)])

while range_to_point(CentroidA, CentroidB) < 0.25:
    CentroidA = np.array([np.random.uniform(0, 1), np.random.uniform(0, 1)])
    CentroidB = np.array([np.random.uniform(0, 1), np.random.uniform(0, 1)])
print(range_to_point(CentroidA,CentroidB))
print(CentroidA)
print(CentroidB)

for x in data.transpose():
    if (range_to_point(CentroidA, x) > range_to_point(CentroidB, x)):
        BaseA.append(x)
    else:
        BaseB.append(x)

CentroidA_old = np.array(CentroidA)
CentroidB_old = np.array(CentroidB)


CentroidA[0] = new_centroid_axis(BaseA[0])
CentroidA[1] = new_centroid_axis(BaseA[1])

CentroidB[0] = new_centroid_axis(BaseB[0])
CentroidB[1] = new_centroid_axis(BaseB[1])


while (CentroidA_old.all() != CentroidA.all()):
    CentroidA_old = np.array(CentroidA)
    CentroidB_old = np.array(CentroidB)

    BaseA = []
    BaseB = []

    for x in data.transpose():
        if (range_to_point(CentroidA, x) > range_to_point(CentroidB, x)):
            BaseA.append(x)
        else:
            BaseB.append(x)

    CentroidA[0] = new_centroid_axis(BaseA[0])
    CentroidA[1] = new_centroid_axis(BaseA[1])

    CentroidB[0] = new_centroid_axis(BaseB[0])
    CentroidB[1] = new_centroid_axis(BaseB[1])


BaseA = np.array(BaseA).transpose()
BaseB = np.array(BaseB).transpose()
plt.plot(BaseA[0], BaseA[1], "ro")
plt.plot(CentroidA[0], CentroidA[1], "gD")
plt.plot(BaseB[0], BaseB[1], "bo")
plt.plot(CentroidB[0], CentroidB[1], "gD")
plt.show()
