#independent test
"""
import numpy as np
from scipy import stats

class_A = [85, 90, 88, 92, 76, 81, 95, 89]
class_B = [78, 82, 80, 85, 79, 84, 88, 83]

t_stat,p_value=stats.ttest_ind(class_A,class_B)

print(f"T-Statistics:{t_stat}")

print(f"p-value:{p_value}")

#যদি p-value < 0.05 হয়, তাহলে দুটি গ্রুপের গড়ের মধ্যে পার্থক্য statistically significant।
#এখানে p-value = 0.048, যা 0.05-এর কম, তাই দুই ক্লাসের নম্বরের মধ্যে পার্থক্য

#2. ANOVA (Analysis of Variance)

import numpy as np
from scipy import stats

# তিনটি ভিন্ন ক্লাসের ছাত্রদের নম্বর
class_X = [85, 89, 76, 91, 88]
class_Y = [79, 81, 77, 83, 80]
class_Z = [92, 95, 89, 90, 93]

f_stat,p_value=stats.f_oneway(class_X,class_Y,class_Z)

print(f"F-Statistic: {f_stat}")
print(f"P-Value: {p_value}")

#p-value = 0.002, যা 0.05-এর কম, তাই গ্রুপগুলোর মধ্যে উল্লেখযোগ্য পার্থক্য আছে।


 #3. Mann-Whitney U Test (Non-parametric Test)

import numpy as np
from scipy import stats

# দুই গ্রুপের নম্বর
group_A = [56, 60, 63, 67, 70]
group_B = [50, 55, 58, 61, 65]

u_stat,p_value=stats.mannwhitneyu(group_A,group_B)

print(f"U-Statistics:{u_stat}")
print(f"p-value:{p_value}")

#p-value = 0.095, যা 0.05-এর বেশি, তাই গ্রুপগুলোর মধ্যে উল্লেখযোগ্য পার্থক্য নেই।


#4. Chi-Square Test (Categorical Data)
import numpy as np
import scipy.stats as stats

# Observed data (ভেজ, নন-ভেজ, ভেগান)
observed = [50, 30, 20]

# Expected সমানভাবে জনপ্রিয় হলে (50 জন করে প্রতিটিতে)
expected = [33.33, 33.33, 33.33]

# Chi-square test
chi_stat, p_value = stats.chisquare(observed, expected)

print(f"Chi-Square Statistic: {chi_stat}")
print(f"P-Value: {p_value}")


#Show statistical description of the values in an array:

import numpy as np
from scipy.stats import describe

v=np.random.normal(size=100)
res=describe(v)

print(res)

#Kurtosis:

import numpy as np
from scipy.stats import skew, kurtosis

v=np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))

#normaltest

import numpy as np
from scipy.stats import normaltest

v=np.random.normal(size=100)

print(normaltest(v))
"""

"""
#k-Test
#from normal distribution

import numpy as np
from scipy.stats import kstest

v=np.random.normal(size=100)

res=kstest(v,'norm')
print(res)

#for UNIFORM distribution

import numpy as np
from scipy.stats import kstest

v=np.random.uniform(size=100)
res=kstest(v,'uniform')
print(res)
"""
#Example 3: Exponential Distribution চেক করা

import numpy as np
from scipy.stats import kstest

v=np.random.normal(scale=1,size=100)

res=kstest(v,'expon')
print(res)