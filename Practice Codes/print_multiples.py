n = 0
m = 0
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
