import numpy as np
import matplotlib.pyplot as plt

def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: a numpy ndarray object
    :return: list
    """
    total = hist.sum()
    norm_hist = list(i/total for i in hist)
    return norm_hist

def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width
    :param histo: list
    :param width: float
    :return: float
    """

    num_samples = histo.sum()
    list_prob = norm_histogram(histo)

    square_sum = 0
    for x in list_prob:
        square_sum += (x*x)
    j = (2/((num_samples - 1) * width)) - ((num_samples + 1) / ((num_samples - 1) * width)) * square_sum
    return j

def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    j_vals = []
    for num_bins in range(min_bins, max_bins + 1):
        width = (maximum - minimum) / num_bins
        hist_list= plt.hist(data, num_bins, (minimum, maximum))[0] #What should I replace 5 with?
        new_ele = compute_j(hist_list, width) #compute_j returns float
        j_vals.append(new_ele)
    return j_vals

def find_min(l):
    """
    takes a list of numbers and returns the mean of the three smallest number in that list and their index.
    return as a tuple i.e. (the_mean_of_the_3_smallest_values,[list_of_the_3_smallest_values])
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        The you should return ((14+15+23)/3,[0,2,4])

    :param l: list
    :return: tuple
    """
    index_list = []
    Sum = 0
    value_list = sorted(l)[:3]
    Sum = sum(value_list)
    mean = Sum / 3
    for i in range(3):
        index_ = l.index(value_list[i])
        index_list.append(index_)
    return mean,index_list

if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
