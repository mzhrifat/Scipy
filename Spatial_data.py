"""
from scipy.spatial import distance

point1=(1,2)
point2=(4,6)

dist = distance.euclidean(point1, point2)

print("Euclidean Distance:",dist)

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

#3d
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D পয়েন্টের একটি সেট
points = np.array([
  [2, 4, 1],
  [3, 4, 2],
  [3, 0, 3],
  [2, 2, 4],
  [4, 1, 5]
])

# Delaunay ট্রায়াঙ্গুলেশন তৈরি করা
simplices = Delaunay(points[:, :2]).simplices  # এখানে শুধু x, y কন্ডিশন ব্যবহার করা হয়েছে

# 3D প্লট তৈরি করা
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# পয়েন্টগুলি 3D তে চিহ্নিত করা
ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='r')

# ত্রিভুজের সীমানা প্লট করা
for simplex in simplices:
    simplex_points = points[simplex]
    ax.plot_trisurf(simplex_points[:, 0], simplex_points[:, 1], simplex_points[:, 2], color='cyan', alpha=0.5)

# গ্রাফ দেখানো
plt.show()

"""


#Convex Hull

import numpy as np

from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull=ConvexHull(points)

hull_points=hull.simplices

plt.scatter(points[:,0],points[:,1])
for simplex in hull_points:
    plt.plot(points[simplex,0],points[simplex,1],'k-',color='r')

plt.show()
#plt.savefig("convex.png",format='png')
