#Statistical Description of Data
"""
import  numpy as np
from scipy.stats import describe

v=np.random.normal(size=100)

res=describe(v)
print(res)
"""

#Example 2: Uniform Distribution এ describe() প্রয়োগ করা
import numpy as np
from scipy.stats import describe

v=np.random.uniform(low=10,high=20,size=100)

res=describe(v)
print(res)