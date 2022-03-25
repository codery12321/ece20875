import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.   
    with open(datapath) as polyread:
        lines = polyread.readlines()
    x = []
    y = []
    for line in lines:
        split_data = line.split(" ")
        #print(data)
        x.append(float(split_data[0]))
        y.append(float(split_data[1])) 	
    
    for d in degrees:
        X = feature_matrix(x, d)
        B = least_squares(X,y)
        paramFits.append(B)
    return paramFits

# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    """
    X = np.zeros((len(x),d+1))
    #print(x)
    for ind, ele in enumerate(x):
        dnew = d
        while dnew >= 0:
            newx = ele**dnew
            X[ind][dnew] = newx
            dnew = dnew - 1
    #print(matrix)
    """
    X = [[ele ** degree for degree in list(range(d+1))[::-1]]for ele in x]
    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    #B = np.linalg.lstsq(X, y, rcond = -1)[0]
    B = np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.matmul(np.transpose(X), y))
    return B


if __name__ == "__main__":
    datapath = "poly.txt"
    degrees = [1, 2, 3, 4, 5]

    paramFits = main(datapath, degrees)
    print(paramFits)
    
with open(datapath) as polyread:
    lines = polyread.readlines()
x = []
y = []
for line in lines:
    split_data = line.split(" ")
    #print(data)
    x.append(float(split_data[0]))
    y.append(float(split_data[1])) 
plt.scatter(x, y)
min_x = min(x)
max_x = max(x)
x_data = np.linspace(min_x, max_x)

y1 = (paramFits[0][0] * x_data)    +  paramFits[0][1]
y2 = (paramFits[1][0] * x_data)**2 + (paramFits[1][1] * x_data) + paramFits[1][2]
y3 = (paramFits[2][0] * x_data)**3 + (paramFits[2][1] * x_data)**2 + (paramFits[2][2] * x_data) + paramFits[2][3]
y4 = (paramFits[3][0] * x_data)**4 + (paramFits[3][1] * x_data)**3 + (paramFits[3][2] * x_data)**2 + (paramFits[3][3] * x_data) + paramFits[3][4]
y5 = (paramFits[4][0] * x_data)**5 + (paramFits[4][1] * x_data)**4 + (paramFits[4][2] * x_data)**3 + (paramFits[4][3] * x_data)**2 + (paramFits[4][4] * x_data) + paramFits[4][5]
plt.plot(x_data, y1, "r--", label = "y1")
plt.plot(x_data, y2, "g--", label = "y2")
plt.plot(x_data, y3, "b^", label = "y3")
plt.plot(x_data, y4, "y--", label = "y4")
plt.plot(x_data, y5, "k--", label = "y5")
plt.title("Problem 1 Data Visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = "upper left")
plt.show()