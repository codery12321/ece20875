def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats

    # Write your code here
    if n <= 0: #check n is a positive number
        return []
    if b == h: #step 2
        print("b and h are the same value")
        return []
    if b > h: #step3
        temp = b
        b = h
        h = temp
    w = (h - b) / n #step6

    hist = [0] * n #step5
    for i in range(n):
        for element in data:
            if b + (i * w) <= element < b + ((i+1) * w) and element != b:
                hist[i] += 1
    return hist
    # return the variable storing the histogram
    # Output should be a list

def happybirthday(name_to_day, name_to_month, name_to_year):
    # name_to_day, name_to_month and name_to_year are dictionaries

    # Write your code here
    month_to_all = {}
    months = name_to_month.values()
    name = name_to_month.keys()
    year = name_to_year.values()
    day = name_to_day.values()
    listname = list(name) #get names
    listmonth = list(months) #get month
    listyear = list(year) #get year
    listday = list(day) # get day
    for i in range(len(listname)):
        age = 2022 - listyear[i]

        month_to_all[listmonth[i]]= (listname[i], (listday[i], listyear[i], age))
    # return the variable storing month_to_all
    # Output should be a dictionary
    return month_to_alls
