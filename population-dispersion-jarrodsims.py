# population-dispersion-jarrodsims.py
"""Calculate measures of dispersion using statistics module"""

import statistics as stats

print('Roll variance equals', stats.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))
print('Roll standard deviation equals', stats.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))
