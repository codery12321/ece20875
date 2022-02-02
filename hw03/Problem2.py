import scipy.stats as stats
import matplotlib.pyplot as plt
from helper import *
import math


def get_coordinates(data, each_dist):
    # Part B
    """
    :param: np.ndarray, str
    :return: np.ndarray, np.ndarray

    This function takes in an array of data and the name of a distribution.
    It then calculates the QQ plot by calling the stats.probplot function with the dataset and the named distribution. The stats.probplot function returns a bizarre data structure: a tuple of two tuples; we're concerned with the two values first tuple in the returned tuple. More concretely, the stats.probplot function returns something with a structure like ((X, Y), (c, d, e)), you will need to return the elements in the position of X and Y from the get_coordinates function (return it as a tuple like (X, Y)).
    """
    # Your code starts here...
    (x,y), extra = stats.probplot(data, dist=each_dist)
    return x, y

def calculate_distance(x, y):
    # Part B
    """
    :param: float, float
    :return: float
    This function takes in two floats and returns the calculated distance. The formula you need to use for this function is (in LaTeX form): $$\sqrt{(x - \frac{x+y}{2})^2 + (y - \frac{x+y}{2})^2}$$ It performs vector projection to the identity line.
    """
    # Your code starts here...
    average = (x + y) / 2
    temp = ((x - average) ** 2) + ((y - average) ** 2)
    ans = math.sqrt(temp)
    return ans


def find_dist(sum_err, dists):
    # Part B
    """
    :param: list[float], list[str]
    :return: str, float
    This function takes in a list of the sum of squared distances and a list of distributions. Your code must find the minimum value in the sum_err list of sums and the distribution at the same index in dists. Returns a tuple that contains the distribution selected and the error calculated.
    """
    # Your code starts here...
    min_index = sum_err.index(min(sum_err))
    return dists[min_index], sum_err[min_index]


def main(data_file):
    """
        Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return 'norm',0.32)
    :param: *.csv file name (str)
    :return: str, float
    """
    # Part B
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(sum_err, dists)


if __name__ == "__main__":
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
    ]:
        print(main(each_dataset))
