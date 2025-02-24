#📝 উদাহরণ ১: Skewness এবং Kurtosis গণনা

import numpy as np
from scipy.stats import skew,kurtosis

v=np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

import numpy as np
from scipy.stats import normaltest

v=np.random.normal(size=100)

print(normaltest(v))