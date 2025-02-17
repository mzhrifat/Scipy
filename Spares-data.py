"""
#Create a CSR matrix from an array:

import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

#sparse metrix method

import numpy as np
from scipy.sparse import csr_matrix

arr=np.array([[0,0,0],[0,0,1],[1,0,2]])

print(csr_matrix(arr).data)

#Counting nonzeros with the count_nonzero() method:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).count_nonzero())

#Removing zero-entries from the matrix with the eliminate_zeros() method:
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat=csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

import matplotlib.mlab
#Eliminating duplicates by adding them:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat=csr_matrix(arr)
mat.sum_duplicates()

print(mat)


#chatgpt example
import numpy as np
from scipy.sparse import coo_matrix

# ডুপ্লিকেট এন্ট্রি সহ একটি স্পার্স ম্যাট্রিক্স তৈরি


row = np.array([0, 0, 1, 1, 1])
col = np.array([0, 0, 1, 1, 1])
data = np.array([2, 3, 4, 5, 6])

mat = coo_matrix((data, (row, col)))  # COO ফরম্যাটে তৈরি

print("Before sum_duplicates():")
print(mat)

mat.sum_duplicates()  # ডুপ্লিকেট এন্ট্রিগুলো যোগ করা

print("After sum_duplicates():")
print(mat)


#Converting from csr to csc with the tocsc() method:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])


newarr=csr_matrix(arr).tocsc()

print(newarr)
"""

import numpy as np
from scipy.sparse import csr_matrix

dense_matrix=np.zeros((1000,1000))

dense_matrix[5,10] =1
dense_matrix[200,500] = 2
dense_matrix[999,999] =3

sparse_matrix = csr_matrix(dense_matrix)

# Dense Matrix এর মেমরি সাইজ (bytes)
dense_size = dense_matrix.nbytes

# Sparse Matrix এর মেমরি সাইজ (bytes)
sparse_size = sparse_matrix.data.nbytes + sparse_matrix.indices.nbytes + sparse_matrix.indptr.nbytes

print(f"Dense Matrix Size: {dense_size / (1024**2):.2f} MB")
print(f"Sparse Matrix Size: {sparse_size / (1024**2):.2f} MB")


#print(sparse_matrix)