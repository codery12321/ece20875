import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Part 1
# Function that normalizes features in training set to zero mean and unit variance.
# Input: training data X_train
# Output: the normalized version of the feature matrix: X, the mean of each column in
# training set: trn_mean, the std dev of each column in training set: trn_std.
def normalize_train(X_train):
    # fill in
    mean = []
    std = []
    for i in range(len(X_train[0])):
        column = X_train[:, i]
        mean.append(np.mean(column))
        std.append(np.std(column))
    
    X = []
    for ele in range(len(X_train)):
        tmp_list = []
        for i in range(len(X_train[0])):
            tmp_list.append(((X_train[ele, i] - mean[i]) / std[i]))
        X.append(tmp_list)
    X = np.array(X)
    return X, mean, std


# Part 2
# Function that normalizes testing set according to mean and std of training set
# Input: testing data: X_test, mean of each column in training set: trn_mean, standard deviation of each
# column in training set: trn_std
# Output: X, the normalized version of the feature matrix, X_test.
def normalize_test(X_test, trn_mean, trn_std):

    # fill in
    X = []
    for ele in range(len(X_test)):
        new_list = []
        len_test = len(X_test[0])
        for i in range(len_test):
            new_list.append(((X_test[ele, i] - trn_mean[i]) / trn_std[i]))
        X.append(new_list)
    X = np.array(X)
    return X


# Part 3
# Function to return a numpy array generated with `np.logspace` with a length
# of 51 starting from 1E^-1 and ending at 1E^3
def get_lambda_range():
    
    # fill in
    lmbda = np.logspace(start=0.1, stop=0.001, endpoint=True, base=10, num=51)

    return lmbda


# Part 4
# Function that trains a ridge regression model on the input dataset with lambda=l.
# Input: Feature matrix X, target variable vector y, regularization parameter l.
# Output: model, a numpy object containing the trained model.
def train_model(X, y, l):

    # fill in
    model = Ridge(alpha = l, fit_intercept = True)
    model.fit(X, y)
    return model


# Part 5
# Function that calculates the mean squared error of the model on the input dataset.
# Input: Feature matrix X, target variable vector y, numpy model object
# Output: mse, the mean squared error
def error(X, y, model):

    # Fill in
    yhat = model.predict(X)
    mse = np.mean(sum((y - yhat) **2))
    return mse


def main():
    # Importing dataset
    # step 1 : read csv
    df = pd.read_csv("AAPL.csv")
    # step 2 : identify the column(s) we want to remove
    remove_features = ["Date"]
    # step 3: create extra column for prediction by shifting
    # rows of `Close` columns by one to obtain next day's closing price
    df["Prediction"] = pd.Series(np.append(df["Close"][1:].to_numpy(), [0]))
    # step 4: drop the last row because it would have invalid value after the shift.
    df.drop(df.tail(1).index, inplace=True)
    # step 5: remove the columns identified in step 2
    df.drop(remove_features, axis=1, inplace=True)
    # step 6: create X by dropping the `Prediction` column
    X = np.array(df.drop(["Prediction"], axis=1))
    # step 7: Store `Prediction` column in y array
    y = np.array(df["Prediction"])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Normalizing training and testing data
    [X_train, trn_mean, trn_std] = normalize_train(X_train)
    X_test = normalize_test(X_test, trn_mean, trn_std)

    # Define the range of lambda to test
    lmbda = get_lambda_range()
    # lmbda = [1,3000]
    MODEL = []
    MSE = []
    for l in lmbda:
        # Train the regression model using a regularization parameter of l
        model = train_model(X_train, y_train, l)

        # Evaluate the MSE on the test set
        mse = error(X_test, y_test, model)

        # Store the model and mse in lists for further processing
        MODEL.append(model)
        MSE.append(mse)

    # Part 6
    # Plot the MSE as a function of lmbda
    plt .plot(lmbda, MSE)# fill in
    plt.xlabel('Lambda')
    plt.ylabel('Mean Squared Error')
    plt.title('MSE vs. Lambda')
    plt.show()

    # Part 7
    # Find best value of lmbda in terms of MSE
    ind =  MSE.index(min(MSE)) # fill in
    [lmda_best, MSE_best, model_best] = [lmbda[ind], MSE[ind], MODEL[ind]]

    print(
        "Best lambda tested is "
        + str(lmda_best)
        + ", which yields an MSE of "
        + str(MSE_best)
    )

    # Part 8
    # Load GOOG.csv similar to steps 1-5 (where AAPL.csv is loaded)
    goog = pd.read_csv("GOOG.csv")
    # step 2 : identify the column(s) we want to remove
    remove_col = ["Date"]
    # step 3: create extra column for prediction by shifting
    # rows of `Close` columns by one to obtain next day's closing price
    goog["Prediction"] = pd.Series(np.append(goog["Close"][1:].to_numpy(), [0]))
    # step 4: drop the last row because it would have invalid value after the shift.
    goog.drop(goog.tail(1).index, inplace=True)
    # step 5: remove the columns identified in step 2
    goog.drop(remove_col, axis=1, inplace=True)
    X = np.array(goog.drop(["Prediction"], axis=1))# complete (similar to step 6)
    y = np.array(goog["Prediction"])  # complete (similar to step 7)

    # normalize X similar to X_test

    X = normalize_test(X, trn_mean, trn_std)
    #print(normX)
    y_hat = model.predict(X)
    #print(y_hat)
    model_best.fit(X, y) 
    plt.plot(y, label = "actual")
    plt.plot(y_hat, label = "prediction")
    plt.legend(loc = "upper left")
    plt.show()
 
    # plot y and y_hat
    return model_best


if __name__ == "__main__":
    model_best = main()
    # We use the following functions to obtain the model parameters instead of model_best.get_params()
    print(model_best.coef_)
    print(model_best.intercept_)
    