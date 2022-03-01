import math as m
import numpy as np
import scipy.stats as stats
from scipy.stats import t
# import or paste dataset here
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

# code for question 1
print('Problem 1 Answers:')
# code below this line
sample_size = len(data)
avg = np.mean(data)
print("sample mean: ", avg)
std_dev = np.std(data, ddof=1)
std_error = std_dev / m.sqrt(sample_size)
print("standard error: ", std_error)

pvalue = 1-0.9
t_score90 = t.ppf(1-pvalue/2, df = sample_size - 1)
print("t_score: ", t_score90)

lvl90_upper = avg + t_score90*(std_error)
lvl90_lower = avg - t_score90*(std_error)
print("lvl90_upper: ", lvl90_upper)
print("lvl90_lower: ", lvl90_lower)
print()

# code for question 2
print('Problem 2 Answers:')
# code below this line
pvalue = 1-0.95
t_score95 = t.ppf(1-pvalue/2, df = sample_size - 1)
print("t_score: ", t_score95)
lvl95_upper = avg + t_score95*(std_error)
lvl95_lower = avg - t_score95*(std_error)
print("lvl95_upper: ", lvl95_upper)
print("lvl95_lower: ", lvl95_lower)
print()

# code for question 3
# code below this line
print('Problem 3 Answers:')

pop_std_dev = 15.836
zvalue = 1.96 #for 95% confidence level
std_err = pop_std_dev / sample_size 
print("standard error: ", std_err)
margin_error = zvalue * pop_std_dev / m.sqrt(sample_size)
upperCL = avg + margin_error
lowerCL = avg - margin_error


print("use z test")
print("population variance = ", pop_std_dev)
print("margin of error: ", margin_error)
print("upper CL: ", upperCL)
print("lower CL: ", lowerCL)
print()
# code for question 4
print('Problem 4 Answers:')
# code below this line
lower = 0
t_score = (avg - lower) / std_error
print("t_score: ", t_score)
p = t.cdf(t_score, df=sample_size-1)
print("p: ", p*100)
