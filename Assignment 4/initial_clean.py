# Name: Tianyu Han
# Student ID: 260890959

import doctest
def which_delimiter(input_string):
    ''' (str) -> str
    This functions takes a string as input and returns the most commonly used delimiiter in
    the input string. It will be one of the space/comma/tab

    >>> which_delimiter('0 1 2, 3')
    ' '
    >>> which_delimiter('0\\t1\\t2, 3')
    '\\t'
    '''
    
    # exception
    if " " not in input_string and "," not in input_string and "\t" not in input_string:
        raise AssertionError("The input string does not contain space/comma/tab.")

    # create helper variables
    number_of_space = 0
    number_of_comma = 0
    number_of_tab = 0

    # use for loop to count how many times each delimiter has occured
    for char in input_string:
        if char == ' ':
            number_of_space += 1
        elif char == ',':
            number_of_comma += 1
        elif char == '\t':
            number_of_tab += 1

    # use max function to find the most commonly used delimiter
    winner = max(number_of_space, number_of_comma, number_of_tab)
    if winner == number_of_space:
        return ' '
    elif winner == number_of_comma:
        return ','
    else:
        return '\t'


def stage_one(input_filename, output_filename):
    ''' (file) -> int
    This function takes two files as input and will open the file with the name
    input_filename and read it line by line. Then change the most common delimiter
    to tab, change all text to be upper case and then change any / or . in the
    dates to hyphens. Then writes the new version of the line to a new file named
    output_filename. This function will return an integer indicating how many
    lines were written to the output file.
    
    >>> stage_one('260890959.txt', 'stage1.tsv')
    3000
    '''
    # open the two files
    in_file = open(input_filename, 'r', encoding = 'utf-8')
    out_file = open(output_filename, 'w+', encoding = 'utf-8')

    # use file.readlines() to create a list containing every line of the input file
    content = in_file.readlines()
    in_file.close()

    # use loop to make changes
    for element in content:
        if which_delimiter(element) != '\\t':
            element = element.replace(which_delimiter(element), '\t')
        element = element.upper()
        if element.count('/') >= 4:
            element = element.replace('/', '-', 4)
        if element.count('.') >= 4:
            element = element.replace('.', '-', 4)
        out_file.write(element) # write the lines to the output file

    # use file.seek() to put the pointer at the first line of the file
    out_file.seek(0)
    
    result = len(out_file.readlines())
    out_file.close()
    return result


def stage_two(input_filename, output_filename):
    '''(file) -> int
    This function takes two files as input and will open the file with the name
    input_filename and read it line by line. And then make changes to the lines
    to make sure every line has 9 columns. Then writes the new version of the
    line to a new file named output_filename. This function will return an integer
    indicating how many lines were written to the output file.

    >>> stage_two('stage1.tsv', 'stage2.tsv')
    3000
    '''
    # open the two files
    in_file = open(input_filename, 'r', encoding = 'utf-8')
    out_file = open(output_filename, 'w+', encoding = 'utf-8')

    # use file.readlines() to create a list containing every line of the input file
    content = in_file.readlines()
    in_file.close()

    # use loop to make changes
    for element in content:
        new_string = ''
        a = element.split('\t')
        while len(a) >= 10:
            if a[6][0] != 'I' and a[6][0] != 'D' and a[6][0] != 'R' and a[6][0] != 'M':
                a[5] = a[5] + ' ' + a[6]
                a.pop(6)
            elif len(a[5]) == 3 and len(a[6]) == 3:
                a[5] = a[5] + a[6]
                a.pop(6)
            else:
                a[7] = a[7] + '.' + a[8]
                a.pop(8)
        if len(a[7]) >= 14:
            a[7] = a[7].replace('.', ' ')
        for units in a:
            new_string += '\t' + units
        out_file.write(new_string[1:]) # write the lines to the output file
        
    # use file.seek() to put the pointer at the first line of the file
    out_file.seek(0)
    result = len(out_file.readlines())
    out_file.close()
    return result
        
    
  

#########################################
if __name__ == '__main__':
    doctest.testmod()
