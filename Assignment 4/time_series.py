# Name: Tianyu Han
# Student ID: 260890959

from datetime import *
import numpy as np
import matplotlib.pyplot as plt
import doctest
def date_diff(date1, date2):
    ''' (str, str) -> int
    This function takes two strings representing dates as input and returns how
    many days apart the two dates are as an integer. If the first date is earlier
    than the second one, the number will be positive; otherwise, it will be negative.

    >>> date_diff('2019-10-31', '2019-11-2')
    2
    >>> date_diff('2018-10-31', '2019-11-2')
    367
    '''
    
    date1_list = date1.split('-')
    date2_list = date2.split('-')
    date1_final = date(int(date1_list[0]), int(date1_list[1]), int(date1_list[2]))
    date2_final = date(int(date2_list[0]), int(date2_list[1]), int(date2_list[2]))
    diff = date2_final - date1_final
    return diff.days


def get_age(date1, date2):
    ''' (str, str) -> int
    This function takes two strings representing dates as input and returns how
    many complete years apart the two dates are as an integer. If the first date
    is earlier than the second one, the number will be positive; otherwise, it
    will be negative.

    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    '''

    diff = date_diff(date1, date2)
    age = int(diff/365.2425)
    return age


def stage_three(input_filename, output_filename):
    '''(file) -> dict
    This function takes two files as input and will open the file with the name
    input_filename and read it line by line. First, take the first date in the
    first line of the file as index date. Then replace the date of each record
    with the date_diff of that date and the index date and replace the date of
    birth with age at the time of the index date. At last, replace the status
    with one of I, R and D.

    Then writes the new version of the line to a new file namedoutput_filename.
    This function will return a dictionary with the keys being each day of the
    pandemic (integer) and the values being a dictionary with how many people
    are in each state on that day.

    >>> stage_three('stage2.tsv', 'stage3.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}, 2: {'I': 6, 'D': 1, 'R': 0}, \
3: {'I': 14, 'D': 4, 'R': 0}, 4: {'I': 41, 'D': 2, 'R': 0}, 5: {'I': 104, 'D': 7, 'R': 0}, \
6: {'I': 216, 'D': 57, 'R': 0}, 7: {'I': 575, 'D': 44, 'R': 5}, 8: {'I': 1447, 'D': 103, 'R': 9}, \
9: {'I': 334, 'D': 25, 'R': 2}}
    '''

    # open the two files
    in_file = open(input_filename, 'r', encoding = 'utf-8')
    out_file = open(output_filename, 'w+', encoding = 'utf-8')

    # use file.readlines() to create a list containing every line of the input file
    content = in_file.readlines()
    in_file.close()

    # determine the index date
    index_date = content[0].split('\t')[2]

    # create some helper variables
    result = {}
    different_dates = []
    sorted_different_dates = []

    # use for loop to make changes to the lines
    for element in content:
        new_string = ''
        a = element.split('\t')
        a[2] = str(date_diff(index_date, a[2]))
        a[3] = str(0 - get_age(index_date, a[3]))
        a[6] = a[6][0]
        if a[6] == 'M':
            a[6] = 'D'
        for units in a:
            new_string += '\t' + units
        out_file.write(new_string[1:]) # write the lines to the output file
        
    out_file.seek(0)
    second_content = out_file.readlines()
    out_file.close()

    # use for loop and a helper variable to sort the keys
    for sub_list in second_content:
        a = sub_list.split('\t')
        different_dates.append(a[2])
        for dates in different_dates:
            if dates not in sorted_different_dates:
                sorted_different_dates.append(dates)

    # use another for loop to create dictionary for each key
    for i in sorted_different_dates:
        sub_dic = {'I': 0, 'D': 0, 'R': 0}
        for sub_list in second_content:
            splitted_string = sub_list.split('\t')
            if splitted_string[2] == i:
                if splitted_string[6] == 'I':
                    sub_dic['I'] += 1
                elif splitted_string[6] == 'D' or splitted_string[6] == 'M':
                    sub_dic['D'] += 1
                else:
                    sub_dic['R'] += 1
                result[int(i)] = sub_dic
    return result
    

def plot_time_series(d):
    ''' (dict) -> list
    This function takes a dictionary of dictionaries as input and return
    a list of lists where each sublist represents each day of the pandemic,
    with the format of [how many people infected, how many people recovered,
    how many people dead].

    >>> d = stage_three('stage2.tsv', 'stage3.tsv')
    >>> plot_time_series(d)
    [[1, 0, 0], [2, 0, 1], [6, 0, 1], [14, 0, 4], [41, 0, 2], [104, 0, 7], \
[216, 0, 57], [575, 5, 44], [1447, 9, 103], [334, 2, 25]]
    '''

    # use dict.values() to get all the values in the input d
    values = list(d.values())
    result = []

    # use for loop to create the list as required
    for element in values:
        new_list = []
        new_list.append(element['I'])
        new_list.append(element['R'])
        new_list.append(element['D'])
        result.append(new_list)

    # use numpy and matplotlib to generate the plot
    x = np.arange(0, 3)
    y = np.arange(0, 11)
    plt.title("Time series of early pandemic, by Tianyu Han")
    plt.xlabel("Days into Pandemic")
    plt.ylabel("Number of People")
    plt.plot(result)
    plt.legend(['Infected', 'Recovered', 'Dead'])
    plt.savefig('time_series')
    return result
        





######################################################
if __name__ == '__main__':
    doctest.testmod()
