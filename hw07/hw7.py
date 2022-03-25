from polyfit import *
"""
separate file to output write up stuff
"""
X = feature_matrix(x, d)
B = least_squares(X,y)
paramFits.append(B)
print("y(1) = %d x + %d", )