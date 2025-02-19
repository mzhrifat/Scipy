"""
from scipy import io
import numpy as np

arr=np.arange(10)

io.savemat('arr.mat',{"vec":arr})
"""

from scipy import io
import numpy as np

arr=np.array([0,1,2,3,4,5,6,7,8,9])

# **Matlab ফরম্যাটে ডেটা এক্সপোর্ট করুন**
io.savemat('arr.mat',{"vec":arr})

#mydata=io.loadmat('arr.mat')
mydata=io.loadmat('arr.mat',squeeze_me=True)

#print(mydata)
print(mydata['vec'])
