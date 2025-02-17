#csr_matrix,csr_graph,Adajacency matrix,Connected components,Dijkstra's Algorithm,Floyd-warshall Ak=lgorithm,Bellman_Ford-Algorithm,Depth-first-Search,Breadth-First-search

"""

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr=csr_matrix(arr)

print(connected_components(newarr))



#dijkstra

import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr=csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))


#Floyd Warshall

import numpy as np
from fontTools.ttLib import newTable
from numpy.ma.core import indices
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr=np.array([
    [0,1,2],
    [1,0,0],
    [2,0,0]
])
newarr=csr_matrix(arr)

print(floyd_warshall(newarr,return_predecessors=True))


#Bellman_ford

import numpy as np
from numpy.testing.print_coercion_tables import print_new_cast_table
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr=np.array([
    [0,-1,2],
    [1,0,0],
    [2,0,0]
])

newarr=csr_matrix(arr)

print(bellman_ford(newarr,return_predecessors=True,indices=0))

#Deeprth first order

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr=np.array([
    [0,1,0,1],
    [1,1,1,1],
    [2,1,0,1],
    [0,1,0,1]
])

newarr=csr_matrix(arr)
print(depth_first_order(newarr,1))

"""
#breadth_first_order

import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix
arr = np.array([
  [0, 1, 0, 1],  # A → B, A → D
  [1, 1, 1, 1],  # B → A, B → B, B → C, B → D
  [2, 1, 1, 0],  # C → A, C → B, C → C
  [0, 1, 0, 1]   # D → B, D → D
])
newarr=csr_matrix(arr)

print(breadth_first_order(newarr,1))

