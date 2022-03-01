import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here
myfile0 = open('engagement_0.txt')
data0 = myfile0.readlines()
#convert elements in data to floats
data0 = [float(x) for x in data0]
myfile1 = open('engagement_1.txt')
data1 = myfile1.readlines()
#convert elements in data to floats
data1 = [float(i) for i in data1]

# Question 1
# null hypo: mean engagement of students who become knowledgeable in the material (i.e., the engagement_1 population) is 0.75
# alt hypo: mean engagement of engagement_1 is not 0.75
# 1 sample T-Test could be used

"""
Report the 
- sample size
- sample mean
- standard error
- standard score 
- p-value
"""
# code for question 2
print('Problem 2 Answers:')
# code below this line
sample_size1 = len(data1)
print('Sample Size: ', sample_size1)
mu1 = 0.75
avg1 = np.mean(data1)
print('Sample Mean: ', avg1)

std_dev1 = np.std(data1, ddof=1)
std_error1 = std_dev1 / m.sqrt(sample_size1)
print('Standard error: ', std_error1)

z_score1 =  avg1 - mu1 / std_error1
print('Standard Score: ', z_score1)

pval1 = stats.ttest_1samp(data1,0.75)[1] #what should the 2nd argument be
print("pvalue: ", pval1)
"""
if (pval1 < 0.01):
    print("reject null hypothesis")
    print("significance level: 0.01")
elif (pval1>0.01 and pval1<0.05):
    print("reject alternative hypothesis.")
    print("significance level: 0.05")
elif (pval1>0.05 and pval1<0.1):
    print("reject alternative hypothesis.")
    print("significance level: 0.1")
"""

# code for question 3 
# basically asking you to calc the std error at 95% conficence lvl
print()
print('Problem 3 Answers:')

# code below this line
pvalue = 0.05
z_c = norm.ppf(pvalue/2)
std_err = (avg1 - mu1) / z_c
size = m.ceil((std_dev1 / std_err)**2)
print("std_err: ", std_err)
print("")

null= "mean engagement is same"
alt = "mean engagement is different"
mu = 0.0
# 2 sample T-Test can be used

# code for question 5
print('Problem 5 Answers:')
# code below this line
sample_size0 = len(data0)
print('Sample Size 0: ', sample_size0)

avg0 = np.mean(data0)
print('Sample Mean 0: ', avg0)

std_dev0 = np.std(data0, ddof=1)
std_err0 = m.sqrt((std_dev0**2/sample_size0) + (std_dev1 **2/sample_size1))
print('Standard error 0: ', std_err0)

zscore0 = (avg0 - avg1) / std_err0
print('Standard Score 0: ', zscore0)

print("ratio less than 4 means population variance is equal. Ratio: ", np.var(data1)/np.var(data0))

pval = 2 * norm.cdf(-abs(zscore0))
print("pvalue: ", pval)
if (pval < 0.01):
    print("reject null hypothesis")
    print("conclusion:", alt)
    print("significance level: 0.01")
elif (pval>0.01 and pval<0.05):
    print("reject alternative hypothesis.")
    print("conclusion:", null)
    print("significance level: 0.05")
elif (pval>0.05 and pval<0.1):
    print("reject alternative hypothesis.")
    print("conclusion:", null)
    print("significance level: 0.1")

myfile0.close()
myfile1.close()
