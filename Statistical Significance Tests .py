#independent test

import numpy as np
from scipy import stats

class_A = [85, 90, 88, 92, 76, 81, 95, 89]
class_B = [78, 82, 80, 85, 79, 84, 88, 83]

t_stat,p_value=stats.ttest_ind(class_A,class_B)

print(f"T-Statistics:{t_stat}")

print(f"p-value:{p_value}")

#যদি p-value < 0.05 হয়, তাহলে দুটি গ্রুপের গড়ের মধ্যে পার্থক্য statistically significant।
#এখানে p-value = 0.048, যা 0.05-এর কম, তাই দুই ক্লাসের নম্বরের মধ্যে পার্থক্য

