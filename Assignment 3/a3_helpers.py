# COMP 202 A3 Part 1
# Name: Tianyu Han
# Student ID: 260890959

import doctest
import random

def flatten_lists(nested):
    ''' (list) -> list
    This function takes any list as an input and replaces any lists inside
    this list with their values. Then return the resulting list.

    >>> flatten_lists([[0], [1, 2], 3])
    [0, 1, 2, 3]
    >>> flatten_lists([[0, 1], [1, 2], 3])
    [0, 1, 1, 2, 3]
    >>> flatten_lists([[0, 1], 3, [1, 2], 3])
    [0, 1, 3, 1, 2, 3]
    '''
    # creating an empty list
    replaced_list  = []
    
    for element in nested:
        if type(element) == list:

            # edge case
            if len(element) == 0:
                continue
            # use list.extend() to add the elements from a list into a list
            replaced_list.extend(element)
        else:

            # use list.append() to add a string or an int into a list
            replaced_list.append(element)
    return replaced_list


def flatten_dict(d):
    ''' (dict) -> list
    This function takes a dictionary as an input and return a list which cotains
    the keys of the dictionary which will repeat v many times where v is the
    value associated with the key in the dictionary.

    >>> flatten_dict({'LIBERAL': 5, 'NDP':2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    >>> flatten_dict({'LIBERAL': 3, 'NDP':2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    '''
    # create an empty list
    new_list = []

    # edge case
    if len(d) == 0:
        return False
    
    # use loop to add the party name into new_list
    for key in d:
        for i in range(d[key]):
            new_list.append(key)
    return new_list
    

def add_dicts(d1, d2):
    ''' (dict, dict) -> dict
    This function takes two dictionaries where all the values are numbers as input
    and merges the two dictionaries. If a key is in both dictionaries, add their
    values. And finally, return the resulting dictionary.
    
    >>> add_dicts({'a':5, 'b':2, 'd':-1}, {'a':7, 'b':1, 'c':5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    >>> add_dicts({'a':5, 'b':2, 'c':-1}, {'a':7, 'd':5, 'b':1})
    {'a': 12, 'b': 3, 'c': -1, 'd': 5}
    '''

    # create an empty dictionary
    resulting_dict = {}


    for key1 in d1:
        if key1 in d2: # compare if key1 is in d2. If so, add their values
            resulting_dict[key1] = d1[key1]+d2[key1]
        else:
            resulting_dict[key1] = d1[key1]
            
    for key2 in d2:
        if key2 not in d1:
            resulting_dict[key2] = d2[key2]
    return resulting_dict

def get_all_candidates(ballots):
    ''' (list) -> list
    This function takes a list as input and return all the unique strings in this
    list and its nested contents.

    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}, \
                           ['CPC', 'NDP'], 'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}, \
                           ['CPC', 'NDP']])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC']
    '''

    # create an empty list 
    results = []

    # copy the input so the input will not be modified
    new_ballots = ballots[:]
    
    for element in new_ballots:

        # edge case
        if len(element) == 0:
            continue
        
        if type(element) == list or type(element) == dict:
            for names in element:
                if names not in results:
                    results.append(names)
                    
        else:
            results.append(element)
            
    return results 


###################################################### winner/loser

def get_candidate_by_place(result, func):
    ''' (dict, func) -> str
    This function evaluate the input function on the dictionary's value. Return
    the key of the dictionary correspoding to that value. Ties will be broken
    randomly.

    >>> random.seed(0)
    >>> get_candidate_by_place({'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4}, min)
    'GREEN'
    >>> random.seed(1)
    >>> get_candidate_by_place({'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4}, min)
    'LIBERAL'
    '''

    # create an empty list
    new_list = []

    # get the values from the input dictionary
    result_values = result.values()

    # edge case
    if len(result_values) == 0:
        return False

    # create an intermediate variable to be compared
    compare_value = func(result_values)
    
    for i in result:
        if result[i] == compare_value:
            new_list.append(i)
    final_result = random.choice(new_list)
    return final_result

def get_winner(result):
    ''' (dict) -> str
    This function evaluate the values of each key in the input dictionary and find
    the maximum value. Return the key of the dictionary correspoding to  value.
    Ties will be broken randomly.
    
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    >>> random.seed(0)
    >>> get_winner({'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4})
    'CPC'
    '''

    # call the helper function
    final = get_candidate_by_place(result, max)
    return final


def last_place(result):
    '''(dict) -> str
    This function evaluate the values of each key in the input dictionary and find
    the minimum value. Return the key of the dictionary correspoding to  value.
    Ties will be broken randomly.

    >>> random.seed(0)
    >>> last_place({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'BLOC'
    >>> random.seed(0)
    >>> last_place({'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4})
    'GREEN'
    '''

    # call the helper function
    final = get_candidate_by_place(result, min)
    return final


###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
