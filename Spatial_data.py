"""
from scipy.spatial import distance

point1=(1,2)
point2=(4,6)

dist = distance.euclidean(point1, point2)

print("Euclidean Distance:",dist)
"""
#Triangulation

import numpy as np
from scipy.spatial import Delaunay, convex_hull_plot_2d
import matplotlib.pyplot as plt

points=np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,1]
])

simplices=Delaunay(points).simplices

plt.triplot(points[:,0],points[:,1],simplices)
plt.scatter(points[:,0],points[:,1],color='r')


plt.title("Delaunay Triangulation Example")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)

plt.savefig("Triangulation.png",format='png')
#plt.show()


