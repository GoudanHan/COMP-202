import doctest
n = 0
m = 0
rows = 0
cols = 0
def print_multiples(n, m):
    ''' (num) -> num
    takes two integers as input n and m
    and prints out the first m multiples of n starting from n
    >>> print_multiples(3, 5)
    3 6 9 12 15
    >>> print_multiples(4, 5)
    4 8 12 16 20
    '''
    
    n = int(input("Please input the first integer n: "))
    m = int(input("Please input the second integer m: "))
    for i in range(m):
        print(n * (i+1), end = " ")

print_multiples(n, m)


def print_mult_table (rows, cols):
    ''' (num) -> num
    takes two integers as input n and m
    and prints out a multiplication table of n rows and m columns
    >>> print_mult_table (2, 3)
    1 2 3
    2 4 6
    >>> print_mult_table (3, 4)
    1 2 3 4
    2 4 6 8
    3 6 9 12
    '''
    rows = int(input("Please input the rows you want to get: "))
    cols = int(input("Please input the columns you want to get: "))
    for row in range(1, rows+1):
        print(print_multiples(row, cols))

print_mult_table(rows, cols)
