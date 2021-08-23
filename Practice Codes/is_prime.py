def prime():

    a = int(input("Please input an integer: "))
    n=2
    if (a < 2):
        return False

    while (n < a):
        if (a%n == 0):
            return False
            n += 1
        else:
            return True


prime()
        
