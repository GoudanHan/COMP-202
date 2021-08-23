# COMP 202 A3
# Name: Tianyu Han
# Student ID: 260890959

from instant_run_off import *

################################################################################

def irv_to_stv_ballot(ballots, num_winners):
    ''' (list, int) -> dict
    This function takes a list and an integer as input and replace each party
    with num_winners many candidates from that party.

    >>> irv_to_stv_ballot([['NDP', 'CPC'], ['GREEN']], 3)
    [['NDP0', 'NDP1', 'NDP2', 'CPC0', 'CPC1', 'CPC2'], ['GREEN0', 'GREEN1', 'GREEN2']]
    >>> irv_to_stv_ballot([['CPC', 'GREEN'], ['BLOC']], 2)
    [['CPC0', 'CPC1', 'GREEN0', 'GREEN1'], ['BLOC0', 'BLOC1']]
    '''

    # create empty lists
    result = []
    final = []
    
    for element in ballots:
        for names in element:
            for i in range(num_winners):
                i = str(i) # cast the integer to string so that it can be added to string
                result.append(names + i)
                
    for n in range(len(ballots)):
        repeat_times = len(ballots[n]) * num_winners
        final.append(result[:repeat_times])
        del result[:repeat_times] # delete the used data to avoid being used repeatedly
        
    return final
        


################################################################################


def eliminate_n_ballots_for(ballots, to_eliminate, n):
    '''(lst, str) -> lst
    Remove n of the ballots in ballots where the first choice is for the candidate to_eliminate.

    Provided to students. Do not edit.

    >>> ballots = [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['GREEN1'], 2)
    [['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3'], 1)
    [['GREEN1', 'GREEN2', 'GREEN3'], ['GREEN1', 'GREEN2', 'GREEN3'], ['NDP3', 'NDP1', 'NDP2', 'GREEN1', 'GREEN2'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> eliminate_n_ballots_for(ballots, ['NDP3', 'GREEN1'], 5)
    [['GREEN1', 'NDP1', 'GREEN2', 'GREEN3'], ['GREEN1', 'NDP1', 'GREEN2', 'GREEN3']]
    >>> b = [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    >>> eliminate_n_ballots_for(b, ['GREEN1'], 2)
    [['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3'], ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']]
    '''
    quota = n
    new_ballots = []
    elims = 0
    for i,b in enumerate(ballots):
        if (elims >= quota) or  (len(b) > 0 and b[0] not in to_eliminate):
            new_ballots.append(b)
        else:
            elims += 1
    return new_ballots



def stv_vote_results(ballots, num_winners):
    '''(lst of list, int) -> dict

    From the ballots, elect num_winners many candidates using Single-Transferable Vote
    with Droop Quota. Return how many votes each candidate has at the end of all transfers.
    
    Provided to students. Do not edit.

    >>> random.seed(3) # make the random tie-break consistent
    >>> g = ['GREEN1', 'GREEN2', 'GREEN3', 'NDP1', 'NDP2', 'NDP3', 'BLOC1']
    >>> n = ['NDP1', 'NDP2', 'GREEN1', 'GREEN2', 'NDP3', 'BLOC1', 'NDP3']
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 2, 'NDP3': 0}
    >>> random.seed(1)
    >>> pr_dict(stv_vote_results([g]*5 + [n]*3, 4))
    {'BLOC1': 0, 'GREEN1': 2, 'GREEN2': 2, 'GREEN3': 0, 'NDP1': 2, 'NDP2': 0, 'NDP3': 0}
    >>> green = ['GREEN', 'NDP', 'BLOC', 'LIBERAL', 'CPC']
    >>> ndp = ['NDP', 'GREEN', 'BLOC', 'LIBERAL', 'CPC']
    >>> liberal = ['LIBERAL', 'CPC', 'GREEN', 'NDP', 'BLOC']
    >>> cpc = ['CPC', 'NDP', 'LIBERAL', 'BLOC', 'GREEN']
    >>> bloc = ['BLOC', 'NDP', 'GREEN', 'CPC', 'LIBERAL']
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 2))
    {'BLOC': 32, 'CPC': 34, 'GREEN': 0, 'LIBERAL': 0, 'NDP': 34}
    >>> pr_dict(stv_vote_results([green]*10 + [ndp]*20 + [liberal]*15 + [cpc]*30 + [bloc]*25, 3))
    {'BLOC': 26, 'CPC': 26, 'GREEN': 0, 'LIBERAL': 22, 'NDP': 26}
    '''
    quota = votes_needed_to_win(ballots, num_winners)

    to_eliminate = []
    result = {}
    final_result = {}

    for i in range(num_winners):
        # start off with quasi-IRV

        result = count_first_choices(ballots)

        while (not has_votes_needed(result, quota)) and len(result) > 0:
            to_eliminate.append( last_place(result) ) 
            ballots = eliminate_candidate(ballots, to_eliminate)
            result = count_first_choices(ballots)

        # but now with the winner, reallocate ballots above quota and keep going
        winner = get_winner(result)
        if winner:
            final_result[winner] = quota # winner only needs quota many votes
            ballots = eliminate_n_ballots_for(ballots, final_result.keys(), quota)
            ballots = eliminate_candidate(ballots, final_result.keys())
            result = count_first_choices(ballots)

    # remember the candidates we eliminated, their count should be 0
    for candidate in to_eliminate:
        final_result[candidate] = 0
    final_result.update(result)
    return final_result


################################################################################


def count_stv(ballots, num_winners):
    ''' (list, int) -> dict
    This function takes a list and an integer as input and returns a dictionary
    indicating how many candidates from each party won this election.

    >>> random.seed(3)
    >>> g = ['GREEN', 'NDP', 'BLOC']
    >>> n = ['NDP', 'GREEN', 'BLOC']
    >>> pr_dict(count_stv([g]*5 + [n]*3, 4))
    {'BLOC': 0, 'GREEN': 3, 'NDP': 1}
    '''

    # convert the ranked ballots to STV result
    result = irv_to_stv_ballot(ballots, num_winners)
    result = stv_vote_results(result, num_winners)

    # create empty dictionary and list
    final_result = {}
    actual_party_names = []

    # get the keys from the dictionary
    party_names = list(result.keys())

    for name in party_names:
        new_name = name[:-1] # get rid of the last number from every candidate's name
        if new_name not in actual_party_names:
            actual_party_names.append(new_name) # add the processed names to the list
            
    for key in result:
        if result[key] != 0:
            if key[:-1] not in final_result:
                final_result[key[:-1]] = 1
                # if it's not in the dictionary, create it and assign value, 1 to it
            else:
                final_result[key[:-1]] += 1
        else:
            if key[:-1] not in final_result:
                final_result[key[:-1]] = 0
                # if it's not in the dictionary and don't win the STV,
                # create it and assign the value, 0 to it
                
    return final_result

################################################################################


def count_SL(results, num_winners):
    ''' (list, int) -> dictionary
    This function takes a list of plurality vote results and an integer as input
    and returns a dictionary indicating how many seats each party won using the
    Sainte-Lague Method.
    
    >>> pr_dict(count_SL(['GREEN', 'LIBERAL', 'NDP', 'LIBERAL', 'BLOC'], 4))
    {'BLOC': 1, 'GREEN': 1, 'LIBERAL': 1, 'NDP': 1}
    >>> pr_dict(count_SL(['GREEN', 'NDP', 'LIBERAL', 'BLOC'], 4))
    {'BLOC': 1, 'GREEN': 1, 'LIBERAL': 1, 'NDP': 1}
    >>> pr_dict(count_SL(['GREEN', 'GREEN', 'NDP', 'LIBERAL', 'BLOC'], 4))
    {'BLOC': 1, 'GREEN': 1, 'LIBERAL': 1, 'NDP': 1}
    >>> pr_dict(count_SL(['A'] * 100000 + ['B'] * 80000 + \
                ['C'] * 30000 + ['D'] * 20000, 8))
    {'A': 3, 'B': 3, 'C': 1, 'D': 1}

    '''

    # call helper function to calculate how many votes each candidate gets
    sum_of_candidates = count_plurality(results)
    
    sum_of_candidates_keys = list(sum_of_candidates.keys())
    sum_of_candidates_values = list(sum_of_candidates.values())

    # assign the value 0 to the candidates
    seats = {}
    for name in sum_of_candidates_keys:
        seats[name] = 0

    # create a dictionary to store the quotient values
    quotient = {}
    for key in sum_of_candidates:
        quotient[key] = sum_of_candidates[key] / (2 * seats[key] + 1)

    for a in range(num_winners-1):
        maximum = max(list(quotient.values())) # intermediate variavle used to be compared
        for i in range(len(sum_of_candidates_keys)):
            if quotient[sum_of_candidates_keys[i]] == maximum:
                variable = sum_of_candidates_keys[i]
                seats[variable] += 1
                quotient[variable] = sum_of_candidates[variable] / (2 * seats[variable] + 1)
                # modify the quotient value

        # use the break to control the loop times
        if sum(list(seats.values())) == num_winners:
            break
        
    return seats
                
    
    


################################################################################


if __name__ == '__main__':
    doctest.testmod()
