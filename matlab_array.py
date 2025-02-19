"""
from scipy import io
import numpy as np

arr=np.arange(10)

io.savemat('arr.mat',{"vec":arr})


from scipy import io
import numpy as np

arr=np.array([0,1,2,3,4,5,6,7,8,9])

# **Matlab ফরম্যাটে ডেটা এক্সপোর্ট করুন**
io.savemat('arr.mat',{"vec":arr})

#mydata=io.loadmat('arr.mat')
mydata=io.loadmat('arr.mat',squeeze_me=True)

#print(mydata)
print(mydata['vec'])


import h5py

# HDF5 MATLAB ফাইল ওপেন করা
file = h5py.File('example_v7_3.mat', 'r')

# ফাইলের কী গুলো দেখা
print(list(file.keys()))

# কোনো নির্দিষ্ট dataset লোড করা
dataset = file['my_matrix'][:]
print(dataset)



from scipy.io import loadmat

# MATLAB .mat ফাইল লোড করা
data = loadmat('vec.mat')

# ফাইলের ভেতরে কী কী ভেরিয়েবল আছে তা দেখা
print(data.keys())

# নির্দিষ্ট কোনো ম্যাট্রিক্স বা অ্যারে পাওয়া
array1 = data['my_matrix']  # 'my_matrix' হলো MATLAB ভেরিয়েবল নাম
print(array1)
"""

from scipy.io import savemat
import numpy as np

# সংরক্ষণের জন্য একটি ডিকশনারি তৈরি
data_to_save = {
    'matrix1': np.array([[1, 2, 3], [4, 5, 6]]),
    'vector1': np.array([10, 20, 30])
}

# .mat ফাইলে সংরক্ষণ
savemat('saved_data.mat', data_to_save)
