# COMP 202 A3
# Name: Tianyu Han
# ID: 260890959

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    ''' (list, int) -> int
    This function takes a list and an int as input and return the interger number
    of votes a candidate would need to win using the Droop Quota.

    >>> votes_needed_to_win([{'CPC':3, 'NDP':5}, {'NDP':2, 'CPC':4}, \
                             {'CPC':3, 'NDP':5}], 1)
    2
    >>> votes_needed_to_win(['g']*20, 2)
    7
    '''

    # edge cases
    if len(ballots) == 0:
        return False
    for names in ballots:
        if len(names) == 0:
            continue
    
    total_votes = len(ballots)

    # use // to round down the number
    result = total_votes // (num_winners + 1) + 1
    
    return result


def has_votes_needed(result, votes_needed):
    ''' (dict, int) -> bool
    This function takes a dictionary and an int as input and return a boolean
    representing whether the candidate with the most votes in this election
    has at least votes_needed votes.


    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 4)
    True
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3, 'CPC': 6}, 5)
    True
    >>> has_votes_needed({'NDP': 4, 'LIBERAL': 3}, 5)
    False
    '''

    # edge case
    if len(result) == 0:
        return False

    # use dict.values() to get all the values in the dictionary
    list_values = result.values()
    
    maximum = max(list_values)
    return maximum >= votes_needed


################################################################################


def eliminate_candidate(ballots, to_eliminate):
    ''' (list, list) -> list
    This function takes two lists as input and return a new list of ranked ballots
    where all the candidates in to_eliminate have been removed.

    >>> eliminate_candidate([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], \
                             ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [[], ['GREEN'], ['BLOC']]
    >>> eliminate_candidate([['NDP', 'LIBERAL', 'BLOC'], ['GREEN', 'NDP'], \
                             ['NDP', 'BLOC']], ['NDP', 'LIBERAL'])
    [['BLOC'], ['GREEN'], ['BLOC']]
    >>> eliminate_candidate([['NDP', 'LIBERAL', 'BLOC'], ['GREEN', 'NDP'], \
                             ['NDP', 'BLOC']], ['NDP', 'LIBERAL', 'GREEN'])
    [['BLOC'], [], ['BLOC']]
    '''

    # create an empty list
    result = []
    
    for element in ballots:
        intermediate = [] # use an intermediate variable to be compared
        
        for names in element:
            if names not in to_eliminate:
                intermediate.append(names) # add the names in the intermediate list
        result.append(intermediate)
    return result

################################################################################


def count_irv(ballots):
    ''' (list) -> dictionary
    This function takes a list of ranked ballots as input and returns a dictionary
    of how many votes each candidate ends with after counting with IRV.

    >>> count_irv([['NDP'], ['GREEN', 'NDP', 'BLOC'], ['LIBERAL','NDP'], \
                   ['LIBERAL'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], \
                   ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP']])
    {'NDP': 5, 'LIBERAL': 3, 'GREEN': 0, 'BLOC': 0, 'CPC': 0}

    >>> count_irv([['GREEN'], ['GREEN', 'NDP', 'BLOC'], ['GREEN','NDP'], \
                   ['GREEN'], ['NDP', 'GREEN'], ['BLOC', 'GREEN', 'NDP'], \
                   ['BLOC', 'CPC'], ['LIBERAL', 'GREEN'], ['NDP'], ['NDP']])
    {'GREEN': 6, 'NDP': 3, 'BLOC': 0, 'CPC': 0, 'LIBERAL': 0}
    '''

    # use helper functions to get some datas
    # that are going to be used in the following codes
    all_candidates = get_all_candidates(ballots)
    needed_votes = votes_needed_to_win(ballots, 1)
    sum_of_first_choices = count_first_choices(ballots)

    # use while loop becasue we don't know the loop times
    while not (has_votes_needed(sum_of_first_choices, needed_votes)):
        # get some datas that are being used in the following codes
        list_values = list(sum_of_first_choices.values())
        list_keys = list(sum_of_first_choices.keys())
        min_list = []
        minimum = min(list_values)
        
        for element in list_values:
            if element == minimum:
                index = list_values.index(element)
                list_values[index] = -1 # in case it's used repeatedly
                min_list.append(list_keys[index])
                
        ballots = eliminate_candidate(ballots, min_list)
        for names in ballots:
            if len(names) == 0:
                names.append('') # edge case
                
        sum_of_first_choices = count_first_choices(ballots)
    if '' in sum_of_first_choices:
        del sum_of_first_choices[''] # delete the empty string in the output
        
    final_keys = list(sum_of_first_choices.keys())
    for candidates in all_candidates:
        if candidates not in final_keys:
            sum_of_first_choices[candidates] = 0
            # add the candidates whose value is 0
            
            
    return sum_of_first_choices


                

        
    


################################################################################

if __name__ == '__main__':
    doctest.testmod()
