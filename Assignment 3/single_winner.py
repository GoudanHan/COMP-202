# COMP 202 A3
# Name: Tianyu Han
# Student ID: 260890959

from a3_helpers import *


def count_plurality(ballots):
    ''' (list) -> dict
    This function takes a list of plurality ballots as input and return a
    dictionary of how many votes each candidate got.

    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    >>> count_plurality(['GREEN', 'LIBERAL', 'NDP', 'LIBERAL', 'BLOC'])
    {'GREEN': 1, 'LIBERAL': 2, 'NDP': 1, 'BLOC': 1}
    '''

    # create an empty dictionary
    result = {}

    # edge case
    if len(ballots) == 0:
        return False

    # copy the input so the input will not be modified
    new_ballots = ballots[:]
    
    for element in new_ballots:
        if element not in result:
            result[element] = new_ballots.count(element)
            # use list.count() to get the total times
            # the element appears in the list
            
    return result
            
        
def count_approval(ballots):
    ''' (list) -> dict
    This function takes a list of approval ballots as input and returns a
    dictionary of how many votes each candidate got.

    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    '''

    # edge case
    if len(ballots) == 0:
        return False
    
    # copy the input so the input will not be modified
    new_ballots = ballots[:]

    # call helper functions
    new_ballots = flatten_lists(ballots)
    result = count_plurality(new_ballots)
    
    return result


def count_rated(ballots):
    ''' (list) -> dict
    This function takes a list of approval ballots as input and returns a
    dictionary of how many points each candidate got.

    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    '''

    # copy the input so the input will not be modified
    new_ballots = ballots[:]
    
    for element in new_ballots:
        
        # edge case
        if len(element) == 0:
            continue
        
        new_ballots[new_ballots.index(element)] = flatten_dict(element)

    # call helper functions
    new_ballots = flatten_lists(new_ballots)
    result = count_plurality(new_ballots)
    return result
        

def count_first_choices(ballots):
    ''' (list) -> dict
    This function takes a list of ranked ballots as input and returns a
    dictionary storing, for every party represented in all the ballots,
    how many ballots for which that party was the first choice


    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']])
    {'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    '''

    # create an empty dictionary
    result = { }

    # copy the input so the input will not be modified
    new_ballots=ballots[:]
    
    candidates = get_all_candidates(new_ballots)
    
    for lists_in_ballots in new_ballots:

        # edge case
        if len(lists_in_ballots) == 0:
            continue
        
        for names in candidates:
            if names == lists_in_ballots[0]:
                if names in result:
                    result[names] += 1 # if names is in the result, add 1 to its value
                else:
                    result[names] = 1 # if not, create this key and assign 1 to its value

    # use loop to get rid of the processed data                
    for key in result:
        candidates.remove(key)

    for element in candidates:
        result[element] = 0
        
    return result

if __name__ == '__main__':
    doctest.testmod()
